from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from .models import Student
from .models import New
from .models import Post


# function based views
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        # check if email already exists
        if Student.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('/')
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        language_list = request.POST.getlist("language")
        language = ",".join(map(str,language_list))
        country = request.POST.get("country")
        image =""
        if request.FILES:
            image = request.FILES['image']
        Student.objects.create(name=name, email=email, phone=phone, gender=gender, language=language, country=country, image=image)
        back = request.META['HTTP_REFERER']
        messages.success(request,'Student added successfully')
        return redirect(back)
    else:
        data = {"studentsData": Student.objects.order_by('-id')}
        return render(request, "index.html", data)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "post_list.html", {'posts':posts})


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


def news(request):
    return render(request, "news.html", {})

def faqs(request):
    return render(request,"faqs.html", {})

