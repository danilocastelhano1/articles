from django.db import models


class Authors(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True, max_length=10)
    name = models.CharField(max_length=120, null=False, verbose_name="Name of the Author")
    picture = models.CharField(max_length=200, default=None, null=True, blank=True, verbose_name="Pic of the Author")
