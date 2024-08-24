from django.db import models
from django.contrib.auth.models import User
from .validator import file_size

# Create your models here.
choice=(
        ('Engish','English'),
        ('Hindi','Hindi'),
    )


class Movies(models.Model):
    
    movie_no = models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=50)
    movie_type = models.CharField(max_length=50)
    release_date = models.DateField()
    quality=models.CharField(max_length=10)
    movie_size =  models.CharField(max_length=50)
    profile = models.ImageField(height_field=None, width_field=None, max_length=None)
    lang = models.CharField(max_length=50, choices=choice)
    movie = models.FileField(upload_to='video/%y',validators=[file_size],null=True)
    