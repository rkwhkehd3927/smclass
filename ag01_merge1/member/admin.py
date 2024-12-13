from django.contrib import admin
from member.models import Member,Star,Reservation

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'nickname', 'mDate']

@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
  list_display = ['sNo','sDate']

@admin.register(Reservation)
class ResAdmin(admin.ModelAdmin):
  list_display = ['rNo','resPeople','resMemo','rDate']
