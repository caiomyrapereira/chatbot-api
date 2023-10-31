from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

class StartChat(models.Model):
    chat = models.TextField(blank=False, null=False)

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

