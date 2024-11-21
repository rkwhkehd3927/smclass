from django.contrib import admin
from member.models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id','name','nickname','mdate']


# admin.site.register(Member,MemberAdmin)

