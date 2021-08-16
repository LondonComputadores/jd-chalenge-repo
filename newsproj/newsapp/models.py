import uuid
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    slug  = models.SlugField(max_length=150, unique=True)


    class Meta:
        verbose_name='Category'
        verbose_name_plural = 'Categories'

        
    def get_absolute_url(self):
            return reverse('categories', args=[self.slug])

            
    def __str__(self):
            return self.title


class Authors(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    picture = models.ImageField(max_length=None)

    def __str__(self):
        return self.name


class Articles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=300)
    firstParagraph = models.TextField(max_length=150)
    body = models.TextField(max_length=6000)
    
    class Meta:
        verbose_name='Articles'
        verbose_name_plural = 'Articles'
        
    def get_absolute_url(self):
        return reverse('articledetails', args=[self.slug])
    
    def __str__(self):
        return self.title
