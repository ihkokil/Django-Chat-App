# ./chat/admin.py
from django.contrib import admin
from .models import UserProfile, chatMessages

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'is_login')
    list_filter = ('gender', 'is_login')
    search_fields = ('user__username', 'user__first_name', 'user__last_name')

@admin.register(chatMessages)
class chatMessagesAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'message_preview', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('message', 'user_from__username', 'user_to__username')
    readonly_fields = ('date_created',)

    def message_preview(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message Preview'
