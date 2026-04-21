from django.db import models

# Create your models here.
class UserReadModel(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = "user_read_model"
        managed = True
