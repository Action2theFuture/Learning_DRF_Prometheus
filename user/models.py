from django.db import models

class User(models.Model):
    email        = models.EmailField(max_length=128, unique=True)
    password     = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "users"
