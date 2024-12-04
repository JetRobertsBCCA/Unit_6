from django.db import models

# Models
class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=2, unique=True)
    state_flower = models.CharField(max_length=255)
    capital_city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

class County(models.Model):
    name = models.CharField(max_length=255)
    county_seat = models.CharField(max_length=255)
    population = models.PositiveIntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='counties')
    #cascade deletes models accociated with it, so that you do not get errors

    def __str__(self):
        return f"{self.name}, {self.state.abbreviation}"

# Functions
def create_state(name, abbreviation, state_flower, capital_city):
    if not name or not abbreviation or not state_flower or not capital_city:
        raise ValueError("All fields are required to create a state.")
    return State.objects.create(
        name=name,
        abbreviation=abbreviation.upper(),
        state_flower=state_flower,
        capital_city=capital_city
    )

def create_county(name, county_seat, population, state):
    if not name or not county_seat or not population or not state:
        raise ValueError("All fields are required to create a county.")
    return County.objects.create(
        name=name,
        county_seat=county_seat,
        population=population,
        state=state
    )

def find_counties_for_state(abbreviation):
    try:
        state = State.objects.get(abbreviation=abbreviation.upper())
        return state.counties.all()
    except State.DoesNotExist:
        raise ValueError("State with the given abbreviation does not exist.")

def state_population(state):
    if not state:
        raise ValueError("State is required.")
    return state.counties.aggregate(total_population=models.Sum('population'))['total_population'] or 0

def counties_containing_state_capital():
    return County.objects.filter(county_seat=models.F('state__capital_city'))
