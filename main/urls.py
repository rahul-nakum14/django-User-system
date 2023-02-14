from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('home/', views.home,name="home"),
    path('sign-up/', views.sign_up,name="sign_up"),
    path('create-post/', views.create_post,name="create-post"),
    path('update-post/<int:post_id>/', views.update_post, name='update-post'),
    path('delete-post/', views.delete_post, name='delete-post'),
]
