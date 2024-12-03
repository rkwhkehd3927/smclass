from django.db import models

class Attendance(models.Model):
  aName = models.CharField(max_length=100)
  attendance = models.CharField(max_length=100)
  aDate = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.aName}"