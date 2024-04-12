from django.urls import path,include
from customerapp import views

urlpatterns = [
    path('home/',views.home),
    path('availableroom/',views.availableroom),
    path('bookroom/',views.bookroom)
]