# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HomeStudent(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'home_student'

#python manage.py inspectdb > models.py

                                                                                                                                           (.venv) ➜  core python manage.py inspectdb > models.py
