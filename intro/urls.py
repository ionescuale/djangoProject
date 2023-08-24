from django.urls import path
from intro import views

urlpatterns =[
    path('first_page/', views.hello, name='first-page'),
    path('show_name/', views.name, name = 'show-name'),
    path('list_of_cars/', views.cars, name = 'list-of-cars'),
    path('list_of_cooking_books/', views.cooking_books, name = 'list-of-cooking-books'),
]


