from django.test import TestCase
from django.contrib.auth.models import User
from .models import Channel, Message, create_channel, create_user, create_message, messages_for, active_users, lurkers

class ChatChannelSystemTests(TestCase):

    def setUp(self):
        self.channel_name = "General"
        self.user1_name = "JohnDoe"
        self.user2_name = "JaneDoe"
        
        self.channel = create_channel(self.channel_name)
        self.user1 = create_user(self.user1_name)
        self.user2 = create_user(self.user2_name)

    def test_create_channel(self):
        channel = Channel.objects.get(name=self.channel_name)
        self.assertEqual(channel.name, self.channel_name)

    def test_create_user(self):
        user = User.objects.get(username=self.user1_name)
        self.assertEqual(user.username, self.user1_name)

    def test_create_message(self):
        message_text = "Hello, everyone!"
        message = create_message(self.user1, self.channel, message_text)

        self.assertEqual(message.text, message_text)
        self.assertEqual(message.user, self.user1)
        self.assertEqual(message.channel, self.channel)

    def test_messages_for(self):
        create_message(self.user1, self.channel, "Message 1")
        create_message(self.user1, self.channel, "Message 2")

        messages = messages_for(self.channel)
        self.assertEqual(messages.count(), 2)

    def test_active_users(self):
        create_message(self.user1, self.channel, "Message 1")

        active = active_users(self.channel)
        self.assertIn(self.user1, active)
        self.assertNotIn(self.user2, active)

    def test_lurkers(self):
        create_message(self.user1, self.channel, "Message 1")

        lurkers_list = lurkers(self.channel)
        self.assertIn(self.user2, lurkers_list)
        self.assertNotIn(self.user1, lurkers_list)

    def test_empty_channel(self):
        messages = messages_for(self.channel)
        self.assertEqual(messages.count(), 0)

        active = active_users(self.channel)
        self.assertEqual(active.count(), 0)

        lurkers_list = lurkers(self.channel)
        self.assertIn(self.user1, lurkers_list)
        self.assertIn(self.user2, lurkers_list)
