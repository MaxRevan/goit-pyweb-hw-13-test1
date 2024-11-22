from django.db import models
from django.conf import settings

class Author(models.Model):
    name = models.CharField(max_length=100)
    born_date = models.DateField(null=True, blank=True) 
    born_location = models.CharField(max_length=100, blank=True) 
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.text



