from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login as make_user_login #to making the new user logged in
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,EditProfileForm,EditUserForm
from .models import Profile


def signup(request):

    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            make_user_login(request,new_user)

            # create profile for the new user
            user_model = User.objects.get(username=request.user.username)
            new_profile = Profile.objects.create(user=user_model)
            new_profile.save()
            return redirect('index')
            
        else: 
            SignUpForm()
            messages.error(request, 'Invalid Informations')
    context = {
        'form':form,
    }
    return render(request , 'users/signup.html',context)


@login_required
def profile_settings(request):
    profile = Profile.objects.get(user=request.user) #getting the user profile
    userform = EditUserForm(instance=request.user)
    profileform = EditProfileForm(instance=profile)
    if request.method == 'POST':
        userform = EditUserForm(request.POST, instance=request.user)
        profileform = EditProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            new_profile = profileform.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return redirect('index')
        else:
            userform = EditUserForm(instance=request.user)
            profileform = EditProfileForm(instance=profile)
    context={
        'userform':userform,
        'profileform':profileform
    }
    return render(request , 'users/settings.html',context)

def profile(request,id):
    profile = get_object_or_404(Profile,id=id)
     
    context = {
        'profile':profile,
    }
    return render(request,'users/profile.html',context)

def follow(requset,id):
    user1 = requset.user
    user2 = Profile.objects.get(id=id)

    if user1 in user2.follower.all():
        user2.follower.remove(user1)    
        user2.follower_num-=1
        user2.save()
        return redirect('index')
    else:
        user2.follower.add(user1)
        user2.follower_num+=1
        user2.save()
        return redirect('index')