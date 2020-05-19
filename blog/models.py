from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # this is for letting django know how to find the path to any specific Post. this is then used by the class create view
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    

