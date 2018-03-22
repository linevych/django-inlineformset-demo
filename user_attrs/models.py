from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAttribute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    att_name = models.CharField(max_length=30)
    score = models.FloatField()
    hidden = models.BooleanField(default=True)
