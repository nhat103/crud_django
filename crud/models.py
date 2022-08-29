from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.IntegerField(primary_key=True, serialize=True)
    username = models.CharField(max_length=25, unique=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)

    class Meta:
        db_table = "users"
