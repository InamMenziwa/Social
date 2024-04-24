from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, Commentform
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def PostCreate(request):
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)  
            new_item.user = request.user
            new_item.save()
            
    else:
        form = PostForm(data=request.GET)  
    
    return render(request, 'posts/postcreation.html', {"form":form})

@login_required
def feed(request):
    comment_form = Commentform() 
    if request.method == "POST":
        form_data = Commentform(data=request.POST)
        new_comment = form_data.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_comment.post = post
        new_comment.save()
    elif request.method == "GET":
       comment_form = Commentform() 
        
    posts = Post.objects.all()
    logged_user = request.user
    return render(request, "posts/feed.html", {"posts":posts, "logged_user":logged_user, "comment_form":comment_form})

def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('feed')
        