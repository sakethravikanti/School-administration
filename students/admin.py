from django.contrib import admin
from .models import Data
# Register your models here.
@admin.register(Data)
class StudentsAdmin(admin.ModelAdmin):
    list_display=('name','grade','marks')
    