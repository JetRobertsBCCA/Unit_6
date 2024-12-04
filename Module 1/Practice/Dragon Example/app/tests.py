from django.test import TestCase
from .models import Dragon, Lair, create_dragon, create_lair, find_lairs_for_dragon, oldest_dragon, lairs_without_dragons

class DragonLairTests(TestCase):

    def setUp(self):
        # Create test data
        self.dragon1 = create_dragon("Smaug", "Red", 500)
        self.dragon2 = create_dragon("Toothless", "Black", 200)

        self.lair1 = create_lair("Lonely Mountain", "North", self.dragon1)
        self.lair2 = create_lair("Hidden World", "South", self.dragon2)
        self.lair3 = create_lair("Abandoned Cave", "West")

    def test_create_dragon(self):
        dragon = create_dragon("Falkor", "White", 1000)
        self.assertEqual(dragon.name, "Falkor")
        self.assertEqual(dragon.color, "White")
        self.assertEqual(dragon.age, 1000)

    def test_create_lair(self):
        lair = create_lair("Sky Fortress", "Sky")
        self.assertEqual(lair.name, "Sky Fortress")
        self.assertEqual(lair.location, "Sky")
        self.assertIsNone(lair.dragon)

    def test_find_lairs_for_dragon(self):
        lairs = find_lairs_for_dragon("Smaug")
        self.assertIn(self.lair1, lairs)
        self.assertNotIn(self.lair2, lairs)
        self.assertNotIn(self.lair3, lairs)

    def test_oldest_dragon(self):
        oldest = oldest_dragon()
        self.assertEqual(oldest, self.dragon1)

    def test_lairs_without_dragons(self):
        lairs = lairs_without_dragons()
        self.assertIn(self.lair3, lairs)
        self.assertNotIn(self.lair1, lairs)
        self.assertNotIn(self.lair2, lairs)
