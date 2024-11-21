from django.db import models

class Member(models.Model):
  id = models.CharField(max_length=50,primary_key=True)
  pw = models.CharField(max_length=100)
  name = models.CharField(max_length=50)
  nickname = models.CharField(max_length=50)
  tel = models.CharField(max_length=50,default='010-1111-1111')
  gender = models.CharField(max_length=10,default='남자')
  hobby = models.CharField(max_length=50,default='game')
  mdate = models.DateTimeField(auto_now=True) # auto_now_add=처음에 입력된 시간 외에 시간 업데이트 X

  def __str__(self):
    return f"{self.id},{self.name},{self.nickname}"