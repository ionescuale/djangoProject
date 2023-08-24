from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    return HttpResponse("Hello World")


def name(request):
    return HttpResponse("My name is Tralalala laaa")


@login_required()
def cars(request):
    list_cars = {
        'all_cars' :[
            {
                "brand": 'VW',
                "model": 'Golf6',
                "year": 2020
            },
            {
                "brand": 'BMW',
                "model": '530',
                "year": 2021
            },
            {
                "brand": 'Audi',
                "model": 'A6',
                "year": 2023
            },
        ]
    }
    return render(request, 'intro/list_of_cars.html', list_cars)


@login_required()
def cooking_books(request):
    list_of_cooking_books = {
        "all_books" :[
            {
                "nume": "Pinch of Noom",
                "autor": "Kate Allison",
                "editura": "bluebird books for life"
            },
            {
                "nume": "The defined Dish",
                "autor": "Alex Snodgrass",
                "editura": "Houghton Mifflin Harcourt"
            },
            {
                "nume": "Two chubby Cubs - Fast and Filling",
                "autor": "James Anderson",
                "editura": "yellow kite"
            },
            {
                "nume": "Slimming Eats",
                "autor": "Siobhan Wightman",
                "editura": "yellow kite"
            },
        ]
    }
    return render(request, "intro/list_of_cooking_books.html", list_of_cooking_books)