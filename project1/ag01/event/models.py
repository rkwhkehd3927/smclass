from django.db import models

class Attendance(models.Model):
  aId = models.CharField(max_length=100)
  count = models.IntegerField(default=0)
  aDate = models.DateTimeField(max_length=100,auto_now=True)
  last_checked = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return f"{self.aId},{self.count}"