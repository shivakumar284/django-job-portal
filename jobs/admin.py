from django.contrib import admin

# Register your models here.
from .models import Job ,Application

class ApplicationAdmin(admin.ModelAdmin):
  list_display=("user","job","applied_at")

admin.site.register(Job)
admin.site.register(Application,ApplicationAdmin)