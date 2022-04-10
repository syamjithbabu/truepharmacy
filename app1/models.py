from django.db import models

# Create your models here.
class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True,default="")
    owner_email = models.CharField(max_length=50)
    owner_password = models.CharField(max_length=10)

    class Meta:
        db_table = 'owner'