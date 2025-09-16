# ./chat/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, blank=True)
    is_login = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'


class chatMessages(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"From {self.user_from.username} to {self.user_to.username}: {self.message[:20]}..."

    class Meta:
        ordering = ['date_created']
