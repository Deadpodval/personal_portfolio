from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
