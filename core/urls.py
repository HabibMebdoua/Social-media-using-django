from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('upload',views.upload,name='upload'),
    path('like/<int:id>',views.post_like,name='like')
]
