from django.db import models

class Gradepoints(models.Model):
    Grade = models.CharField(primary_key=True,max_length=20, unique=True)
    Points = models.IntegerField()
    Status = models.CharField(max_length=1, choices=[('P', 'Pass'), ('F', 'Fail')])
    Presence = models.CharField(max_length=7, choices=[('PRESENT', 'Present'), ('ABSENT', 'Absent')])

class Branchcodes(models.Model):
    Branch=models.CharField(max_length=100)
    Code=models.CharField(primary_key=True,max_length=2,unique=True)
    Abbrevation=models.CharField(max_length=10)