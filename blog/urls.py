from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('about/', about, name='about'),
    path('post/', PostCreate.as_view(), name='post'),
    path('postDetail/<slug:slug>/', PostDetail.as_view(), name='postDetail'),
    path('postUpdate/<slug:slug>/', PostUpdate.as_view(), name='postUpdate'),
    path('postDelete/<slug:slug>/', PostDelete.as_view(), name='postDelete'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('profile/', profile, name='profile'),
    path('editProfile/', editProfile, name='editProfile'),
    path('addAvatar/', addAvatar, name='addAvatar'),
    path('logout/', logout_user, name='logout'),
]
