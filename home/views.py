from django.shortcuts import render , HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    #For contact
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        phone_no = request.POST['Phone Number']
        message = request.POST['Message']
        contact = Contact(name=name , email=email , phone_no=phone_no , message=message)
        contact.save()

    return render(request,'home/contact.html')

