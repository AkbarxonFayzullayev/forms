from django.db import models

class Fanlar(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=150)
    phone = models.IntegerField()
    location = models.TextField(max_length=150)
    fan = models.ForeignKey(Fanlar,on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname
