from django.db import models
from board.models import Board
from member.models import Member

class Comment(models.Model):
  cno = models.AutoField(primary_key=True)
  board = models.ForeignKey(Board,on_delete=models.CASCADE) # 게시글(부모)이 삭제되면 댓글(자식)도 자동 삭제
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING)
  cPw = models.CharField(max_length=10,null=True,blank=True)
  cContent = models.TextField(blank=True) # 공백 글이 있어도 입력 가능
  cdate = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.cno},{self.cContent},{self.cdate}"