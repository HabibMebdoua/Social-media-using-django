from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    # login
    path('signin',LoginView.as_view(template_name='users/signin.html'),name='signin'),
    # logout
    path('logout',LogoutView.as_view(),name='logout'),
    # Profile settings Page
    path('settings',views.profile_settings,name='settings'),
    path('profile/<int:id>',views.profile,name='profile'),
    # following
    path('follow/<int:id>',views.follow,name='follow')
]
