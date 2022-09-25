from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'updated_on')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'message')
    search_fields = ['user', 'message']

admin.site.register(Post, PostAdmin)
admin.site.register(Avatar)
admin.site.register(Contact, ContactAdmin)