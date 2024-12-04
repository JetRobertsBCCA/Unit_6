from django.db import models

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=100, unique=True)
    monthly_price = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"{self.name}({self.monthly_price})"
    
class Show(models.Model):
    name = models.CharField(max_length=100, unique= True)
    desc = models.CharField(max_length= 300)
    genre = models.CharField(max_length=100)
    seasons = models.PositiveBigIntegerField()
    service = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name= "shows", null=True, blank=True)
    
    def __str__(self):
        return f"{self.name},{self.desc},{self.genre},{self.seasons},{self.service.name}"
    
#==============FUNCTIONS==============

def create_streaming_platform(name, monthly_price):
    if not name or not monthly_price:
        raise ValueError("Error, all fields required")
    return StreamingPlatform.objects.create(name = name, monthly_price = monthly_price)

def create_show(name,desc, genre, service):
    if not name or not desc or not genre or not service:
        raise ValueError("hell naw")
    return Show.objects.create(name = name, desc = desc, genre = genre, seasons = 1 , service = service)

def add_new_season(name):
    x = Show.objects.filter(name = name)
    if x is not None:
        for i in x:
            i.seasons += 1
            i.save()
            return i.seasons
    
def where_to_watch(name):
    x = Show.objects.filter(name = name)
    for i in x:
        return i.service.name
    
def what_to_watch(service, genre):
    try:
        return Show.objects.filter(service = service, genre = genre)
    except Show.DoesNotExist:
        return None

def total_shows(service):
    return Show.objects.filter(service = service)