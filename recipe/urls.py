from django.urls import path
from .import views



urlpatterns = [
    path('recipeHome/',views.recipeHome,name='recipeHome'),
    # path('blogPost/<int:id>/',views.blogPost,name='blogPost'),

]