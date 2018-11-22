
from django.db import models

# Create your models here
#.
class TodoItem(models.Model):
  order = models.IntegerField(null=True, blank=True)
  title = models.CharField(max_length=256, null=True, blank=True)
  completed = models.BooleanField(blank=True, default=False)
  url = models.CharField(max_length=256, null=True, blank=True)
