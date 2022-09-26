from django.urls import path
from .views import *

urlpatterns = [
    path('', chat, name='chat'),
    path('sent/', sent, name='sent'),
    path('send/', SendView.as_view(), name='send'),
]
