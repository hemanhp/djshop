from django.contrib.admin.models import LogEntry
from django.db import models

# Create your models here.
# class FootPrint(models.Model):
#     pass

class ActionHistory(LogEntry):
    class Meta:
        proxy =True

