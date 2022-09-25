from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import *
from django.urls import reverse_lazy


class PostList(ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'postDetail.html'


class PostCreate(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PostCreateForm()}
        return render(request, 'post.html', context)

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            slug = post.title
            post.slug = slug.replace(' ', '-').lower()
            post.save()
            return redirect(reverse_lazy('postDetail', args=[post.slug]))
        return render(request, 'post.html', {'form': form})


class PostUpdate(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['img', 'title', 'subtitle', 'body']
    labels = {
        "img": "Imagen",
        "title": "Título",
        "subtitle": "Subtítulo",
        "body": "Cuerpo",
    }
    template_name = 'postUpdate.html'

    def test_func(self):
        post = get_object_or_404(Post, slug=self.kwargs["slug"])
        return self.request.user == post.author


class PostDelete(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = "postDelete.html"

    def test_func(self):
        post = get_object_or_404(Post, slug=self.kwargs["slug"])
        return self.request.user == post.author


def about(request):
    return render(request, 'about.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'message': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'login.html', {'form': form, 'message': 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user, 'img': getAvatar(request), 'posts': getPosts(request)})


def getPosts(request):
    posts = Post.objects.filter(author=request.user)
    if len(posts) != 0:
        post = posts
    else:
        post = "Aún no tienes posts"
    return post


@login_required
def editProfile(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.password1 = form.cleaned_data['password1']
            user.password2 = form.cleaned_data['password2']
            user.save()
            return redirect('profile')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'editProfile.html', {'form': form, 'user': user, 'img': getAvatar(request)})


@login_required
def addAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            oldAvatar = Avatar.objects.filter(user=request.user)
            if (len(oldAvatar) > 0):
                oldAvatar.delete()
            avatar = Avatar(user=request.user, img=form.cleaned_data['img'])
            avatar.save()
            return redirect('profile')
    else:
        form = AvatarForm()
    return render(request, 'addAvatar.html', {'form': form, 'user': request.user, "img": getAvatar(request)})


def getAvatar(request):
    avatarList = Avatar.objects.filter(user=request.user)
    if len(avatarList) != 0:
        img = avatarList[0].img.url
    else:
        img = ""
    return img


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            message = form.cleaned_data['message']
            contact = Contact(user=user, message=message)
            contact.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


class ContactView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': ContactForm()}
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect(reverse_lazy('contact'))
        return render(request, 'contact.html', {'form': form, 'success': "Mensaje enviado"})
