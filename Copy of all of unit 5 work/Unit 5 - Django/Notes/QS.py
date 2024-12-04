from django.db import models
from django.test import TestCase
from datetime import datetime, timedelta


# ExampleModel Definition
class ExampleModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    age = models.IntegerField(null=True, blank=True)


# Test Case for Field Lookups
class FieldLookupsTest(TestCase):
    def setUp(self):
        ExampleModel.objects.create(
            name="Example One", description="A test case", age=25, created_at=datetime(2024, 11, 16, 14, 30)
        )
        ExampleModel.objects.create(
            name="example two", description="Another test", age=30, created_at=datetime(2024, 11, 17, 10, 15)
        )
        ExampleModel.objects.create(
            name="Final Test", description="Testing endswith", age=None, created_at=datetime(2024, 11, 18, 12, 45)
        )

    def test_field_lookups(self):
        today = datetime(2024, 11, 16).date()

        # Text-based Lookups
        self.assertEqual(ExampleModel.objects.filter(name__contains="Example").count(), 1)
        self.assertEqual(ExampleModel.objects.filter(name__icontains="example").count(), 2)
        self.assertEqual(ExampleModel.objects.filter(name__endswith="Test").count(), 1)
        self.assertEqual(ExampleModel.objects.filter(name__iendswith="test").count(), 2)
        self.assertEqual(ExampleModel.objects.filter(name__startswith="Example").count(), 1)
        self.assertEqual(ExampleModel.objects.filter(name__istartswith="example").count(), 2)

        # Exact Matching
        self.assertEqual(ExampleModel.objects.filter(name__exact="Example One").count(), 1)
        self.assertEqual(ExampleModel.objects.filter(name__iexact="example one").count(), 1)

        # Null Values
        self.assertEqual(ExampleModel.objects.filter(age__isnull=True).count(), 1)

        # Membership
        self.assertEqual(ExampleModel.objects.filter(age__in=[25, 30, 35]).count(), 2)

        # Comparisons
        self.assertEqual(ExampleModel.objects.filter(age__gt=20).count(), 2)
        self.assertEqual(ExampleModel.objects.filter(age__gte=25).count(), 2)
        self.assertEqual(ExampleModel.objects.filter(age__lt=30).count(), 1)
        self.assertEqual(ExampleModel.objects.filter(age__lte=30).count(), 2)

        # Date/Time Lookups
        self.assertEqual(ExampleModel.objects.filter(created_at__date=today).count(), 1)
        self.assertEqual(ExampleModel.objects.filter(created_at__day=16).count(), 1)
        self.assertEqual(ExampleModel.objects.filter(created_at__hour=14).count(), 1)
        self.assertEqual(ExampleModel.objects.filter(created_at__minute=30).count(), 1)
        self.assertEqual(ExampleModel.objects.filter(created_at__month=11).count(), 3)
        self.assertEqual(ExampleModel.objects.filter(created_at__second=0).count(), 3)
        self.assertEqual(ExampleModel.objects.filter(created_at__time=datetime(2024, 11, 16, 14, 30).time()).count(), 1)
        self.assertEqual(ExampleModel.objects.filter(created_at__week=46).count(), 3)
        self.assertEqual(ExampleModel.objects.filter(created_at__week_day=7).count(), 1)  # Saturday
        self.assertEqual(ExampleModel.objects.filter(created_at__iso_week_day=6).count(), 1)  # Saturday
        self.assertEqual(ExampleModel.objects.filter(created_at__year=2024).count(), 3)
        self.assertEqual(ExampleModel.objects.filter(created_at__iso_year=2024).count(), 3)
        self.assertEqual(ExampleModel.objects.filter(created_at__quarter=4).count(), 3)

        # Range
        self.assertEqual(ExampleModel.objects.filter(age__range=(20, 30)).count(), 2)

        # Regex
        self.assertEqual(ExampleModel.objects.filter(name__regex=r'^Example.*').count(), 1)
        self.assertEqual(ExampleModel.objects.filter(name__iregex=r'^example.*').count(), 2)
