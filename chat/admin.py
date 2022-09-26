from django.contrib import admin
from .models import *

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reciever', 'msg_content')
    search_fields = ['sender', 'reciever', 'msg_content']

admin.site.register(Message, MessageAdmin)
