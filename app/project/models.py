from django.db import models

from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=128)
    url_rep = models.URLField(max_length=300, blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField()
