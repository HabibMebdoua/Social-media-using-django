from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    caption = models.TextField(max_length=1200)
    post_img = models.ImageField(upload_to='posts',default='user.png')
    created_date = models.DateTimeField(auto_now_add=True)
    likes_num = models.IntegerField(default=0)
    like = models.ManyToManyField(User, blank=True )
    
    def __str__(self):
        return self.caption

class PostLike(models.Model):
    user = models.ForeignKey(User,related_name='user_post_likes',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='post_likes',on_delete=models.CASCADE)