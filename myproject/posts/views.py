from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.text import slugify
import random
import string


from .models import Post
from .forms import PostForm  # ✅ Import the PostForm

def posts_list(request):
    posts = Post.objects.all().order_by('-published_date')  # ✅ Use the correct field
    return render(request, "posts/posts_list.html", {"posts": posts})

def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug)  # ✅ Use get_object_or_404 to handle errors
    return render(request, "posts/posts_page.html", {"post": post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # Handle image uploads
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign logged-in user as the author
            post.save()  # Save the post first without the slug

            # Ensure unique slug
            base_slug = slugify(post.title)
            slug = base_slug
            count = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1

            post.slug = slug
            post.save()  # Save again with the slug

            return redirect(reverse("posts:posts"))  # Redirect to the post list page
    else:
        form = PostForm()

    return render(request, "posts/post_new.html", {"form": form})
