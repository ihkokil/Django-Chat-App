# ./chat/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import chatMessages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserModel
from django.db.models import Q
import json

@login_required
def home(request):
    User = get_user_model()
    users = User.objects.all()
    chats = []
    chat_id = 0
    selected_user = None # <-- Add this to hold the user object we are chatting with

    if request.method == 'GET' and 'u' in request.GET:
        try:
            chat_id = int(request.GET['u'])
            # Find the selected user object
            selected_user = User.objects.get(id=chat_id)
            # Fetch the chat messages
            chats = chatMessages.objects.filter(
                Q(user_from=request.user, user_to=chat_id) |
                Q(user_from=chat_id, user_to=request.user)
            ).order_by('date_created')
        except (ValueError, User.DoesNotExist): # Use 'User' from get_user_model()
            chat_id = 0
            chats = []
            selected_user = None

    context = {
        "page": "home",
        "users": users,
        "chats": chats,
        "chat_id": chat_id,
        "selected_user": selected_user # <-- Pass the selected user object
    }
    return render(request, "chat/home.html", context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}!')
            return redirect('chat-login')
    else:
        form = UserRegistrationForm()

    context = {
        "page": "register",
        "form": form
    }
    return render(request, "chat/register.html", context)


@login_required
def profile(request):
    context = {
        "page": "profile",
    }
    return render(request, "chat/profile.html", context)


def get_messages(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)

    try:
        last_id = int(request.POST.get('last_id', 0))
        chat_id = int(request.POST.get('chat_id', 0))
    except ValueError:
        return JsonResponse({'error': 'Invalid ID format'}, status=400)

    if chat_id <= 0:
        return JsonResponse({'error': 'Invalid chat ID'}, status=400)

    # Ensure the chat_id corresponds to an existing user (security)
    if not UserModel.objects.filter(id=chat_id).exists():
        return JsonResponse({'error': 'Chat user does not exist'}, status=400)

    chats = chatMessages.objects.filter(
        Q(id__gt=last_id),
        (Q(user_from=request.user.id, user_to=chat_id) |
         Q(user_from=chat_id, user_to=request.user.id))
    ).order_by('id') # Order by ID for consistent polling

    new_msgs = []
    for chat in chats:
        data = {
            'id': chat.id,
            'user_from': chat.user_from.id,
            'user_to': chat.user_to.id,
            'message': chat.message,
            'date_created': chat.date_created.strftime("%b-%d-%Y %H:%M")
        }
        new_msgs.append(data)
    return JsonResponse(new_msgs, safe=False)


def send_chat(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'failed', 'message': 'Invalid request method'}, status=400)

    try:
        user_from_id = int(request.POST['user_from'])
        user_to_id = int(request.POST['user_to'])
        message_text = request.POST['message'].strip()

        if not message_text:
             return JsonResponse({'status': 'failed', 'message': 'Message cannot be empty'}, status=400)

        # Verify users exist (security check)
        u_from = UserModel.objects.get(id=user_from_id)
        u_to = UserModel.objects.get(id=user_to_id)

        # Ensure sender is the logged-in user (security check)
        if u_from != request.user:
             return JsonResponse({'status': 'failed', 'message': 'Unauthorized sender'}, status=403)

        chat_message = chatMessages(user_from=u_from, user_to=u_to, message=message_text)
        chat_message.save()

        return JsonResponse({'status': 'success', 'message_id': chat_message.id})

    except (ValueError, UserModel.DoesNotExist, KeyError) as e:
        # Log the error `logger.error(f"Send chat error: {e}")`
        return JsonResponse({'status': 'failed', 'message': 'Invalid data provided'}, status=400)
    except Exception as e:
        # Log the error `logger.error(f"Unexpected send chat error: {e}")`
        return JsonResponse({'status': 'failed', 'message': 'An internal error occurred'}, status=500)
# Note: In production, consider adding rate limiting and more robust error handling/logging