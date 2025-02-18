from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts'),  # ✅ Posts list
    path("<slug:slug>", views.post_page, name='page'),  # ✅ Post details
    path("new/", views.post_new, name='post_new'),  # ✅ Create new post
]
