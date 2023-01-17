from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, null=False)
    flag = models.CharField(max_length=300)
    continent = models.CharField(max_length=100)
    created_by = models.ForeignKey('user.User', models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)