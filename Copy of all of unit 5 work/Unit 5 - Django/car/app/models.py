from django.db import models

from dataclasses import dataclass

@dataclass
class Car:
    id: int
    name: str        
    make: str        
    year: int       
    description: str 