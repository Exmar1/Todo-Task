from django.contrib import admin
from .models import TaskItem

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
	readonly_fields = ('create_at',)

admin.site.register(TaskItem, TodoAdmin)