from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
import os
import sys
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
        language = ",".join(map(str, language_list))
        country = request.POST.get("country")
        image = ""
        if request.FILES:
            image = request.FILES['image']
        Student.objects.create(name=name, email=email, phone=phone,
                               gender=gender, language=language, country=country, image=image)
        back = request.META['HTTP_REFERER']
        messages.success(request, 'Student added successfully')
        return redirect(back)
    else:
        contact_list = Student.objects.order_by("-id")
        paginator = Paginator(contact_list, 5)  # Show 5 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            "studentsData": page_obj
        }
        return render(request, "index.html", data)


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "post_list.html", {'posts': posts})


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


def news(request):
    return render(request, "news.html", {})


def faqs(request):
    return render(request, "faqs.html", {})


def delete_file(id):
    student = Student.objects.get(id=id)
    if student.image:
        file_path = os.getcwd() + "/uploads/" + str(student.image)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        else:
            return True
    else:
        return True


def delete(request, id):
    if delete_file(id) and Student.objects.get(id=id).delete():
        messages.success(request, "Student deleted successfully")
        return redirect("/")
    else:
        messages.error(request, "Something went wrong")
        return redirect("/")


def edit(request, id):
    if request.method == "POST":
        student = Student.objects.get(id=id)
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.gender = request.POST.get("gender")
        student.language = ",".join(map(str, request.POST.getlist("language")))
        if request.FILES:
            delete_file(id)
            student.image = request.FILES["image"]
        student.country = request.POST.get("country")
        student.save()
        messages.success(request, "Student updated successfully")
        return redirect("/")

    else:
        data = {
            "studentsData": Student.objects.get(id=id)

        }
        return render(request, "update.html", data)
