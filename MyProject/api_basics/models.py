from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


# class User(models.Model):
#     objects = models.Manager()
#
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#
#     def __str__(self):
#         return self.name
