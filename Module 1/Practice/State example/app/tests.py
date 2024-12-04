from django.test import TestCase
from .models import State, County, create_state, create_county, find_counties_for_state, state_population, counties_containing_state_capital

class StateCountyTests(TestCase):

    def setUp(self):
        self.state1 = create_state("Mississippi", "MS", "Magnolia", "Jackson")
        self.state2 = create_state("Alabama", "AL", "Camellia", "Montgomery")

        self.county1 = create_county("Hinds", "Jackson", 250000, self.state1)
        self.county2 = create_county("Rankin", "Brandon", 150000, self.state1)
        self.county3 = create_county("Montgomery", "Montgomery", 230000, self.state2)

    def test_create_state(self):
        state = create_state("Florida", "FL", "Orange Blossom", "Tallahassee")
        self.assertEqual(state.name, "Florida")
        self.assertEqual(state.abbreviation, "FL")
        self.assertEqual(state.state_flower, "Orange Blossom")
        self.assertEqual(state.capital_city, "Tallahassee")

    def test_create_county(self):
        county = create_county("Leon", "Tallahassee", 290000, self.state1)
        self.assertEqual(county.name, "Leon")
        self.assertEqual(county.county_seat, "Tallahassee")
        self.assertEqual(county.population, 290000)
        self.assertEqual(county.state, self.state1)

    def test_find_counties_for_state(self):
        counties = find_counties_for_state("MS")
        self.assertIn(self.county1, counties)
        self.assertIn(self.county2, counties)
        self.assertNotIn(self.county3, counties)

    def test_state_population(self):
        population = state_population(self.state1)
        self.assertEqual(population, 400000)  # 250000 + 150000

    def test_counties_containing_state_capital(self):
        counties = counties_containing_state_capital()
        self.assertIn(self.county1, counties)  # Jackson is the capital of MS and county seat of Hinds
        self.assertIn(self.county3, counties)  # Montgomery is the capital of AL and county seat of Montgomery
        self.assertNotIn(self.county2, counties)
