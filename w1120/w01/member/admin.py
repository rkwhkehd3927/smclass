from django.contrib import admin
from member.models import Member


class MemberAdmin(admin.ModelAdmin):
  list_display = ['id'] # 보통 pw를 보이게하지는 않음
  # list_display = ['id','pw','name','nickname','cdate'] # 보통 pw를 보이게하지는 않음

admin.site.register(Member,MemberAdmin)