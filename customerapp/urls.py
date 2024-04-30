from django.urls import path,include
from customerapp import views

urlpatterns = [
    path('home/',views.home),
    path('availableroom/',views.availableroom),
    path('bookroom/',views.bookroom),
    path('bookingdetails/',views.bookingdetails),
    path('editprofile/',views.editprofile),
    path('deletebooking/',views.deletebooking),
    path('changepassword/',views.changepassword),
    path('search/',views.searchhotel),
    path('logout/',views.Logout),
    path('payment/',views.payment),
]