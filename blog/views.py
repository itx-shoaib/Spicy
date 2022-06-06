from django.shortcuts import render , HttpResponse , redirect
from .models import Post , Comment


# Create your views here.
def blogHome(request):
    post = Post.objects.all()
    content = {'post':post}
    return render(request,'blog/blogHome.html',content)

def blogPost(request,id):
    blog = Post.objects.filter(post_id=id)[0]
    # print(post)
    comments = Comment.objects.all()
    content = {'blog' : blog , 'comments': comments }
    return render(request,'blog/blogPost.html', content )

# API for comments
def comment(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        comments = Comment(name=name,email=email,message=message)
        comments.save()


    return redirect('/')