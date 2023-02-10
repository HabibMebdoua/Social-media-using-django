from django.db import models

from django.contrib.auth.models import User


location = [
    ('ALG','Algeria'),
    ('OUT','Not From Algeria')
]


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    bio = models.TextField(null=True,max_length=1000)
    location = models.CharField(choices=location,max_length=100)
    profile_img = models.ImageField(upload_to='profile_imgs',default='user.png')
    
    follower = models.ManyToManyField(User,related_name='user_follow',blank=True)
    follower_num = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.user.username