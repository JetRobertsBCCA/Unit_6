from django.db import models

# Models
class Dragon(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.color})"

class Lair(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    dragon = models.ForeignKey(Dragon, on_delete=models.SET_NULL, related_name='lairs', null=True, blank=True)

    def __str__(self):
        return f"{self.name} in {self.location}"

# Functions
def create_dragon(name, color, age):
    if not name or not color or not age:
        raise ValueError("All fields are required to create a dragon.")
    return Dragon.objects.create(name=name, color=color, age=age)

def create_lair(name, location, dragon=None):
    if not name or not location:
        raise ValueError("Name and location are required to create a lair.")
    return Lair.objects.create(name=name, location=location, dragon=dragon)

def find_lairs_for_dragon(dragon_name):
    try:
        dragon = Dragon.objects.get(name=dragon_name)
        return dragon.lairs.all()
    except Dragon.DoesNotExist:
        raise ValueError("Dragon with the given name does not exist.")

def oldest_dragon():
    return Dragon.objects.order_by('-age').first()

def lairs_without_dragons():
    return Lair.objects.filter(dragon__isnull=True)
