from django.db import models

# Create your models here.
class Todo_data(models.Model):
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()

    def __str__(self):
        return self.todo_title