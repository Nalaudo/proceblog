from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reciever")
    msg_content = RichTextField()
    created_at = models.DateTimeField(auto_now=True)
