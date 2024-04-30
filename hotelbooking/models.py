from django.db import models
from django.utils import timezone

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200,default="")
    dob = models.DateField(max_length=10)
    status = models.IntegerField(default=0)
    role = models.CharField(default="customer",max_length=10)
    forgot_password_token = models.CharField(max_length=200,default="")

    date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7},{8},{9}".format(self.customer_id,self.name, self.email,self.password,self.mobile,self.gender,self.address,self.dob,self.status,self.role,self.date)



class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=100)
    hotel_img = models.CharField(max_length=100)
    hotel_city = models.CharField(max_length=100)
    hotel_address=models.CharField(max_length=100)
    hotel_rating = models.IntegerField(default=3)
    hotel_price = models.FloatField(max_length=15)
    hotel_discount = models.FloatField(max_length=15)
    hotel_old_price = models.FloatField(max_length=15)

    def __str__(self):
        return self.hotel_name    

class Room(models.Model):
    customer = models.ForeignKey(
        Customer,
        related_name='room',
        on_delete=models.CASCADE,
    ) 
    hotel = models.ForeignKey(
        Hotel,
        related_name='hotel',
        on_delete=models.CASCADE
    )
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=100)
    room_img = models.CharField(max_length=100)
    room_price = models.FloatField(max_length=15)
    room_bed = models.IntegerField(default=0)
    room_bath = models.IntegerField(default=0)
    room_wifi = models.CharField(max_length=5)
    room_description = models.CharField(max_length=200) 
    room_rating = models.IntegerField(default=2)

    def __str__(self):
        return self.room_name    

class Booking(models.Model):
    customer = models.ForeignKey(Customer,
        related_name='customer',
        on_delete=models.CASCADE
    )   
    hotel = models.ForeignKey(Hotel,
        related_name='bookhotel',
        on_delete=models.CASCADE
    )  
    room = models.ForeignKey(Room,
        related_name='bookroom',
        on_delete=models.CASCADE
    )
    hotel_name=models.CharField(max_length=100,default="") 
    room_name=models.CharField(max_length=100,default="") 
    booking_id = models.AutoField(primary_key=True)
    checkin = models.DateTimeField('checkin time')
    checkout = models.DateTimeField('checkout time')
    adult = models.IntegerField(default=0)
    child = models.IntegerField(default=0)
    name = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,default="")
    specialrequest = models.CharField(max_length=200,default="")
    price = models.FloatField(default=0.0)


    def __str__(self):
        return self.customer.name
