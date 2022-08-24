from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)

    class Meta:
        db_table = "users"
