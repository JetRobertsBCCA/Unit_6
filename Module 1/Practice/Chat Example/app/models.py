from django.db import models
from django.contrib.auth.models import User

# =================Models=======================
class Channel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.user.username} in {self.channel.name}"

# ==================Functions======================
def create_channel(name):
    if not name:
        raise ValueError("A channel must have a name.")
    return Channel.objects.create(name=name)

def create_user(username):
    if not username:
        raise ValueError("A user must have a name.")
    return User.objects.create_user(username=username)

def create_message(user, channel, text):
    if not user or not channel or not text:
        raise ValueError("A message must have a user, a channel, and some text content.")
    return Message.objects.create(user=user, channel=channel, text=text)

def messages_for(channel):
    return Message.objects.filter(channel=channel).order_by('created_at')

def active_users(channel):
    return User.objects.filter(message__channel=channel).distinct()

def lurkers(channel):
    active_users_set = active_users(channel)
    return User.objects.exclude(id__in=active_users_set.values_list('id', flat=True))

