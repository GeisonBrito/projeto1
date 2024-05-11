from django.db import models

class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)

class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    complete = models.BooleanField(default=False)