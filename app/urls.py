from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .utils.index import *




urlpatterns = [

    path("",index,name='index'),
    path("base",base,name='base'),
    path("NewPost",NewPost,name='NewPost'),
    path('post/<int:post_id>/details/',image_detail, name='image_detail'),




]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)