from django.db import models

# Create your models here.

## 오라클에서 table 생성가능, insert,update,select,delete
## 오라클에 접속하지 않고, table 생성가능
## orm ( object_relational mapping ) 객체 관계형 매핑

class Student(models.Model): # students > Student
  s_name = models.CharField(max_length=100)
  s_major = models.CharField(max_length=100)
  s_age = models.IntegerField(default=0)
  s_grade = models.IntegerField(default=0)
  s_gender = models.CharField(max_length=30)

  def __str__(self): # class Student 를 호출하면 자동으로 얘도 호출
    return self.s_name 