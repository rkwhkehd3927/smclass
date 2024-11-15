from django.apps import AppConfig

# StudentsConfig = 최초로 실행되는 파일
class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
