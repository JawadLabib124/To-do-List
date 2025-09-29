from django.db import models

# Create your models here.

class Tasks(models.Model):
    NewTask=models.CharField(max_length=50,null=False)
    Description=models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.NewTask