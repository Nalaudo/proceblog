from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from chat.forms import MessageForm
from chat.models import Message
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def chat(request):
    return render(request, 'chat.html', {'messages': getMessageInbox(request).order_by('-created_at')})


def getMessageInbox(request):
    messages = Message.objects.filter(reciever=request.user)
    if len(messages) != 0:
        message = messages
    else:
        message = 0
    return message


@login_required
def sent(request):
    return render(request, 'sent.html', {'messages': getMessageSent(request).order_by('-created_at')})


def getMessageSent(request):
    messages = Message.objects.filter(sender=request.user)
    if len(messages) != 0:
        message = messages
    else:
        message = 0
    return message


class SendView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': MessageForm()}
        return render(request, 'send.html', context)

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.sender = self.request.user
            post.save()
            return redirect(reverse_lazy('sent'))
        return render(request, 'sent.html', {'form': form})
