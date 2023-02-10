from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,PostLike
from users.models import Profile
# Create your views here.

@login_required
def index(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.get(user = profile.follower)

    context = {
        'posts':posts,
    }
    return render(request , 'core/index.html',context)

def upload(request):
    # creating a new post
    if request.method == 'POST':
        user = request.user
        post_img = request.FILES.get('post_img')
        caption = request.POST['post_caption']

        new_post = Post.objects.create(
            user = user,
            caption = caption,
            post_img = post_img,
        )
        new_post.save()
        return redirect('index')
    return redirect('index')

def post_like(request,id):
    user = request.user
    post = Post.objects.get(id=id)
    if user in post.like.all():
        post.like.remove(user)
        post.likes_num-=1
        post.save() 
        return redirect('index')
    else:
        post.like.add(user)
        post.likes_num+=1
        post.save()
        return redirect('index')
         
                    # 2 nd way to liking
    # like_filter = PostLike.objects.filter(user=user,post_id=post.id).first()

    # if like_filter == None:
    #     new_like = PostLike.objects.create(user=user,post=post)
    #     new_like.save()
    #     post.likes+=1
    #     post.save() 
    #     return redirect('index')
    # else:
    #     like_filter.delete()
    #     post.likes-=1
    #     post.save() 
    #     return redirect('index')



