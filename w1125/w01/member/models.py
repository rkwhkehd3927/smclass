from django.db import models


class Member(models.Model):
  id = models.CharField(max_length=50,primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  nickname = models.CharField(max_length=100)
  tel = models.CharField(max_length=20,default='010-0000-0000')
  gender = models.CharField(max_length=10,default='남자')
  hobby = models.CharField(max_length=50,default='game')
  mdate = models.DateTimeField(auto_now=True)


# from datetime import datetime
  # mdate = models.DateTimeField(default=datetime.now())
# import datetime
  # mdate = models.DateTimeField(default=datetime.datetime.now())

  def __str__(self):
    return f"{self.id},{self.name},{self.mdate}"