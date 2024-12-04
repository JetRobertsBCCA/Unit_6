from django.shortcuts import render
from .models import Car


cars = [
    Car(id=1, name="Mustang", make="Ford", year=1965, description="A classic American muscle car with a powerful V8 engine."),
    Car(id=2, name="Model S", make="Tesla", year=2020, description="A sleek, electric car with cutting-edge technology and autonomous driving features."),
    Car(id=3, name="Civic", make="Honda", year=2018, description="A reliable and fuel-efficient compact car popular for city driving."),
    Car(id=4, name="New Cawr", make="vroom", year= 132, description="wow it go really fast and makes loud noises. This car weally be the beast!")
]

def car_list(request):
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = next((car for car in cars if car.id == car_id), None)
    return render(request, 'car_detail.html', {'car': car})
