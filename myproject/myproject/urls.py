from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('posts/', include("posts.urls", namespace="posts")),
    path('users/', include("users.urls")),  # Ensure users.urls is included
]

    # Serve media files during development
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
