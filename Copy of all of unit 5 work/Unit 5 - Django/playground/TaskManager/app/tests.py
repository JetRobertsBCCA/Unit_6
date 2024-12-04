from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from datetime import datetime, timedelta
from .models import Task
from .models import (
    create_task,
    all_tasks,
    find_task_by_title,
    completed_tasks,
    update_task_completion,
    delete_task,
)


class TaskManagerTest(TestCase):
    def setUp(self):
        # Create sample tasks
        self.task1 = create_task(
            title="Complete project report",
            description="Finish the report by Monday",
            due_date=datetime.now().date() + timedelta(days=3),
        )
        self.task2 = create_task(
            title="Prepare for meeting",
            description="Gather all necessary documents",
            due_date=datetime.now().date() - timedelta(days=1),
            is_completed=True,
        )
        self.task3 = create_task(
            title="Buy groceries",
            description="Purchase milk, bread, and eggs",
            due_date=datetime.now().date() + timedelta(days=7),
        )

    def test_create_task(self):
        task = create_task(
            title="Learn Django",
            description="Study Django models and queries",
            due_date=datetime.now().date(),
        )
        self.assertEqual(task.title, "Learn Django")

    def test_all_tasks(self):
        tasks = all_tasks()
        self.assertEqual(tasks.count(), 3)

    def test_find_task_by_title(self):
        task = find_task_by_title("Prepare for meeting")
        self.assertIsNotNone(task)
        self.assertEqual(task.description, "Gather all necessary documents")

    def test_completed_tasks(self):
        tasks = completed_tasks()
        self.assertEqual(tasks.count(), 1)
        self.assertEqual(tasks.first().title, "Prepare for meeting")

    def test_update_task_completion(self):
        task = update_task_completion("Buy groceries", True)
        self.assertTrue(task.is_completed)

    def test_delete_task(self):
        delete_task("Complete project report")
        tasks = all_tasks()
        self.assertEqual(tasks.count(), 2)
