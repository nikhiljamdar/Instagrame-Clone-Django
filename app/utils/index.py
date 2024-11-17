from django.shortcuts import render
from ..models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

# from post.models import Post, Tag, Follow, Stream, Likes
from django.contrib.auth.models import User
from app.forms import NewPostform
# from authy.models import Profile
from django.urls import resolve
# from comment.models import Comment
# from comment.forms import NewCommentForm
from django.core.paginator import Paginator

from django.db.models import Q


# Create your views here.



def index(request):
    posts = Post.objects.all()  # Or filter for a specific post if needed
    
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)



def base(request):
    return render(request, 'base.html')




# @login_required
def NewPost(request):
    print('innnnnnn')
    user = request.user  # Use the User instance directly
    print('nikhillllll')

    # profile = get_object_or_404(Profile, user=user)
    tags_obj = []
    
    if request.method == "POST":
        form = NewPostform(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tags')
            tag_list = list(tag_form.split(','))

            for tag in tag_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_obj.append(t)
                
            # Use the user instance here
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user=user)
            p.tags.set(tags_obj)
            p.save()
            return redirect('index')
    else:
        form = NewPostform()
    
    context = {
        'form': form
    }
    return render(request, 'newpost.html', context)


def image_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'image_detail_popup.html', context)