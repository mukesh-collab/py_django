from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ Auto-login after registration
            messages.success(request, "Registration successful. You are now logged in!")
            return redirect("posts:posts")
        else:
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect to 'next' if provided, otherwise redirect to /posts/new/
            next_page = request.GET.get('next', '/posts/')
            messages.success(request, "You have successfully logged in!")
            return redirect(next_page)
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("posts:posts")  # ✅ Redirects to Posts Page after Logout
