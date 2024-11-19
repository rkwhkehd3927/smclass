from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=100)
  major = models.CharField(max_length=100)
  grade = models.IntegerField(default=0)
  age = models.IntegerField(default=0)
  gender = models.CharField(max_length=10)
  hobby = models.CharField(max_length=50)

  def __str__(self): # 문자열
    return f"{self.name},{self.major},{self.grade}" 