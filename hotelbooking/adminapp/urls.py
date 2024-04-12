from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('home/',views.home),
    path('addroom/',views.addroom),
    path('viewroom/',views.viewroom),
    path('addhotel/',views.addhotel),
    path('viewhotel/',views.viewhotel)
]