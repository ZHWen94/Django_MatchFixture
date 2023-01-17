from django.db import models

class Match(models.Model):
    team1_id = models.ForeignKey('country.Country', related_name="team1_id", on_delete=models.CASCADE)
    team2_id = models.ForeignKey('country.Country', related_name="team2_id", on_delete=models.CASCADE)
    match_date = models.DateField()
    venu = models.CharField(max_length=100)
    created_by = models.ForeignKey('user.User', models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)