from django.shortcuts import render

# Create your views here.
def recipeHome(request):
    return render(request,'recipe/recipeHome.html')