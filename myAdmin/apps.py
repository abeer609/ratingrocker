from django.apps import AppConfig
from django.contrib import admin

class MyadminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myAdmin'


