from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.ForeignKey('country.Country', on_delete=models.CASCADE)
    image = models.CharField(max_length=300)
    dob = models.DateField()
    status = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.FloatField()
    created_by = models.ForeignKey('user.User', models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)