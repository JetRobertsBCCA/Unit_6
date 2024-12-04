from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    due_date = models.DateField
    is_completed = models.BooleanField()


#Task Functions
def create_task(title, description, due_date, is_completed=False):
    return Task.objects.create(title = title, description = description, due_date = due_date, is_completed = is_completed)

def all_tasks():
    return Task.objects.all()

def find_task_by_title(title):
    try:
        return Task.objects.get(title = title)
    except Task.DoesNotExist:
        return None
    
def completed_tasks():
    return Task.objects.filter(is_completed = True)

def update_task_completion(title, is_completed):
    task = find_task_by_title(title)
    if task is not None:
        task.is_completed = is_completed
        task.save()

def delete_task(title):
    task = find_task_by_title(title)
    if task is not None:
        task.delete()

def tasks_due_within_7_days():
    today = datetime.now().date()
    return Task.objects.filter(due_date__range=(today, today + timedelta(days=7)))