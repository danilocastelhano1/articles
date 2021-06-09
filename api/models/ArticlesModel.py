from django.db import models

from .AuthorsModel import Authors


class Articles(models.Model):
    id = models.AutoField(primary_key=True, max_length=10)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, null=False)
    category = models.CharField(max_length=60, null=False, verbose_name="Category of the Article")
    title = models.CharField(max_length=60, null=False, verbose_name="Title of the Article")
    summary = models.TextField(default=None, null=True, verbose_name="summary of the Article")

    def __str__(self):
        return self.title
