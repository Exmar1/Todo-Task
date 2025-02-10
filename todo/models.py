from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskItem(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	important = models.BooleanField(default=False)
	create_at = models.DateTimeField(auto_now_add=True)
	datecompleted = models.DateTimeField(null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title 