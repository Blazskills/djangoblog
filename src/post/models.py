from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



User = get_user_model()

class Author (models.Model):
    user = models.OneToOneField(User , on_delete =models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)


    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    # overview = RichTextField(blank=True, null = True)
    overview = RichTextUploadingField(blank=True, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    comment_count = models.IntegerField(default= 0)
    view_count = models.IntegerField(default= 0)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })
