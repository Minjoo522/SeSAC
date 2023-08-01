from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=True)
    create_date = models.DateTimeField(null=True)
    update_date = models.DateTimeField(null=True)