from django.db import models

# Create your models here.
class crudModel(models.Model):
    user_name=models.CharField(max_length=100)
    user_address=models.CharField(max_length=100)
    user_mobilenumber=models.CharField(max_length=10)

    def __str__(self):
        return "user_name={0},user_address={1},user_mobilenumber={2}".format(self.user_name,self.user_address,self.user_mobilenumber)