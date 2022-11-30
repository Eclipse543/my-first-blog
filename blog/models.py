from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Student(models.Model):
    gender_field = (("male", "Male"), ("female", "Female"))
    language_field = (
        ("nepali", "Nepali"),
        ("english", "English"),
        ("chinese", "Chinese"),
    )
    country_field = (
        ("nepal", "Nepal"),
        ("india", "India"),
        ("china", "China"),

    )
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, unique=True, null=True)
    phone = models.CharField(max_length=200, unique=True,null=True)
    gender = models.CharField(choices=gender_field, max_length=10,null=True)
    language = models.CharField(choices=language_field, max_length=100,null=True)
    country = models.CharField(choices=country_field, max_length=100,null=True)
    image = models.ImageField(upload_to='students/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_language(self):
        return self.language.split(",")

class New(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    published_date = models.DateTimeField(auto_now_add=True, null=True)
