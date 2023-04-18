from django.db import models
from core.models import PublishedModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(PublishedModel):
    title = models.CharField(max_length=256,)
    text = models.TextField()
    pub_date = models.DateTimeField()
    authour = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL
    )   
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL
    )


class Category(PublishedModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)


class Location(PublishedModel):
    name = models.CharField(max_length=256)
