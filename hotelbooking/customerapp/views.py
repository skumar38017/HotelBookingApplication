from django.shortcuts import render
from hotelbooking.models import Customer,Room,Hotel
# Create your views here.
from django.conf import settings

curl = settings.BASE_URL
media_url=settings.MEDIA_URL

def home(request):
    listofdic=Customer.objects.filter(email="rahulsharma@gmail.com",password="12345").values()
    print(listofdic[0])

    #====get image======#
   
    # qs=Room.objects.all()
    # room_data = qs.values()
    # print(room_data)

    qs=Hotel.objects.all()
    hotel_data = qs.values()
    print(hotel_data)
   
    #====get image======#
    if request.method == "GET": 
       return render(request,'CustomerHome.html',{'customer':listofdic[0],'media_url':media_url,'hotel_data':hotel_data})


def availableroom(request):
    listofdic=Customer.objects.filter(email="rahulsharma@gmail.com",password="12345").values()
    print(listofdic[0])
    if request.method == "GET":
       id=request.GET.get('id') 
       print("Hotel Id:",id)
       availablerooms = Room.objects.filter(hotel_id=id).values()
       print("Rooms======>",availablerooms)
       return render(request,'AvailableRoom.html',{'customer':listofdic[0],'media_url':media_url,"availablerooms":availablerooms})

def bookroom(request):
        listofdic=Customer.objects.filter(email="rahulsharma@gmail.com",password="12345").values()
        print(listofdic[0])
        if request.method == "GET":
            id=request.GET.get('id') 
            return render(request,'BookRoom.html',{'customer':listofdic[0],'media_url':media_url})