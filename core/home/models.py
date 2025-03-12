from django.db import models

# Create your models here.



class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'home_student'
