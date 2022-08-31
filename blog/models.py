from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='thumbnail/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    summary = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
