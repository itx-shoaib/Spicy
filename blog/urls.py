from django.urls import path
from .import views



urlpatterns = [
    # API for comments
    path('comment',views.comment,name='comment'),


    path('blogHome/',views.blogHome,name='blogHome'),
    path('blogPost/<int:id>/',views.blogPost,name='blogPost'),

]