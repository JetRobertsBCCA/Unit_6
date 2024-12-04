from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
import random

def hello_view(request: HttpRequest):
    return HttpResponse("Hello World")

def roll_view(request: HttpRequest, sides):
    roll = random.randint(1, sides)
    return HttpResponse(roll)

def warmup1_view(request: HttpRequest, n):
    if (n >=90 and n <=110) or (n>= 190 and n<=210):
        return HttpResponse("True")
    else:
        return HttpResponse("False")
    
def warmup2_view(request: HttpRequest, input_str):
    result = ''.join([input_str[:i] for i in range(1, len(input_str) +1)])
    return HttpResponse(result)

def warmup3_view(request: HttpRequest, input_str):
    cat_count = input_str.count('cat')
    dog_count = input_str.count('dog')
    result = cat_count == dog_count
    return HttpResponse(result)

def warmup4_view(request: HttpRequest, a,b,c):
    result = 0 
    if a != b and a != c:
        result += a
    if b != a and b != c:
        result += b
    if c != a and c != b:
        result += c
    return HttpResponse(result)


