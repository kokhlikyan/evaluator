from django.db import models


class Operation(models.Model):
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
