from django.db import models

class Otp(models.Model):
    user = models.ForeignKey('user.User', models.DO_NOTHING)
    otp_val = models.IntegerField()