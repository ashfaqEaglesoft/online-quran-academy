from django.shortcuts import redirect, render
from .models import slider,Enroll,Team,Tesmonial,Contact
# Create your views here.

def index(request):
    slides=slider.objects.all()
    team=Team.objects.all()
    tesmonial=Tesmonial.objects.all()

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        country=request.POST.get('country')
        gender=request.POST.get('gender')
        en=Enroll(fullname=name,email=email,mobile=phone,country=country,gender=gender)
        en.save()

    context={
        'slider':slides,
        'team':team,
        'tesmonial':tesmonial,
    }
    return render(request,'index.html',context)


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        con=Contact(name=name,email=email,subject=subject,msg=message)
        con.save()
    return redirect("/")

