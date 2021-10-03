from django.shortcuts import render, HttpResponse      # time 2:37:13
from .models import Contact
from django.http import HttpResponse

# password for this user is  Dev905775 , username - Devendra

# superuser :- username= devendra , password:- dev905775

# Create your views here.
def index(request):

    #  index.html, contact us code, 
    if request.method=="POST":
        contact = Contact()
        name = request.POST.get('name', '')      
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject =request.POST.get('subject', '')
        message =request.POST.get('message', '')
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.subject=subject
        contact.message=message
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT US</h1>")

    return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')    

# def drop1(request):
#     return render(request, 'drop1.html')    

# def drop2(request):
#     return render(request, 'drop2.html')

# def drop3(request):
#     return render(request, 'drop3.html')

# def drop4(request):
#     return render(request, 'drop4.html')    

# def index(request):
#     return render(request, 'index.html')