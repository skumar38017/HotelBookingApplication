from django.shortcuts import render,redirect
from hotelbooking.models import Customer,Room,Hotel,Booking
#for logout
from django.contrib.auth import logout

#django payment
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.http import HttpResponseBadRequest

# Create your views here.
from django.conf import settings

curl = settings.BASE_URL
media_url=settings.MEDIA_URL
import time


 


def sessioncheckcustomer_middleware(get_response):
    def middleware(request):
        print("============= request=====:",request.path)
        strpath = request.path
        list1 = strpath.split("/")
        if len(list1)>2:
            strnewpath = "/"+list1[1]+"/"+list1[2]+"/"
            if strnewpath=='/customer/home/' or strnewpath=='/customer/bookingdetails/' or strnewpath=='/customer/editprofile/' or strnewpath == '/customer/changepassword/' or strnewpath == '/changepassword/' or strnewpath == '/forgotpassword/' :
                if 'emailid' not in request.session:            
                 response=redirect('http://localhost:8000/login')
                else:
                    response=get_response(request)
            else:
                response=get_response(request)
        else:
            return get_response(request)        
        return response
        
    return middleware 



def home(request):
    emailid=request.session.get("emailid")
    password=request.session.get("password") 
    listofdic=Customer.objects.filter(email=emailid,password=password).values()
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
        emailid=request.session.get("emailid")
        password=request.session.get("password") 
        listofdic=Customer.objects.filter(email=emailid,password=password).values()
        print(listofdic[0])
       
        if request.method == "GET":
            r_id=request.GET.get('id')
            h_id=request.GET.get('h_id') 
            return render(request,'BookRoom.html',{'customer':listofdic[0],'media_url':media_url})
        elif request.method == "POST":
            print("====================POST")
            name = request.POST['name']
            email = request.POST['email']
            checkin = request.POST['checkin']
            checkout = request.POST['checkout']
            adult = request.POST['adult']
            child = request.POST['child']
            specialrequest = request.POST['specialrequest']
            tup_checkin = time.strptime(checkin, '%m/%d/%Y %H:%M %p') 
            checkin=time.strftime("%Y-%m-%d %H:%M:%S",tup_checkin)

            tup_checkout = time.strptime(checkout, '%m/%d/%Y %H:%M %p') 
            checkout=time.strftime("%Y-%m-%d %H:%M:%S",tup_checkout)
            
            #YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
            print(name,email,checkin,checkout,adult,child,specialrequest)
            r_id=request.GET.get('id')
            h_id=request.GET.get('h_id') 
            c_id=listofdic[0]["customer_id"]
            print(c_id,r_id,h_id)
            customer=Customer.objects.get(email=emailid,password=password)
            r_id=int(r_id)
            h_id=int(h_id)
            roomobj=Room.objects.get(room_id=r_id)
            hotelobj=Hotel.objects.get(hotel_id=h_id)
            print(roomobj,hotelobj)
            roomdic=Room.objects.filter(room_id=r_id).values()

            booking = Booking(customer=customer,hotel=hotelobj,room=roomobj,name=name,email=email,checkin=checkin,checkout=checkout,adult=adult,child=child,specialrequest=specialrequest,hotel_name=hotelobj,room_name=roomobj,price=roomdic[0]["room_price"])
            msg=""
            try:
                booking.save()
                msg="Booking Done Successfully"
            except Exception as e:
                print("Error Occured at Booking Hotel:",e)
                msg="Booking Failed, Please try again"
        return render(request,'BookRoom.html',{"curl":curl,"msg":msg})
        
        
def bookingdetails(request):
    
    emailid=request.session.get("emailid")
    password=request.session.get("password") 
    c_id=request.session.get("customer_id") 
    listofdic=Customer.objects.filter(email=emailid,password=password).values()
    print(listofdic[0])
    qs=Booking.objects.filter(customer_id=c_id).values()
    print(qs)
    
    return render(request,'BookingDetails.html',{"curl":curl,'bookingdetails':qs,'customer':listofdic[0]})

def editprofile(request):
    emailid=request.session.get("emailid")
    password=request.session.get("password") 
    listofdic=Customer.objects.filter(email=emailid,password=password).values()
    print(listofdic[0])
    if request.method == "GET":
        return render(request,'EditProfile.html',{'customer':listofdic[0],"curl":curl})
    
    elif request.method == "POST":
        c_id=listofdic[0]["customer_id"]
        c_email=listofdic[0]["email"]
        c_password=listofdic[0]["password"]
        print("====================POST")
        name = request.POST['name']
        mobile = request.POST['mobile']
        address = request.POST['address']
        gender = request.POST['gender']
        dob = request.POST['dob']
        print(name,mobile,address,dob,gender)
        customer = Customer(customer_id=c_id,name=name,email=c_email,password=c_password,mobile=mobile,address=address,gender=gender,dob=dob)
        msg=""
        try:
            customer.save()
            msg="Profile Updated Successfully"
        except Exception as e:
            print("Error Occured at Updating Profile:",e)
            msg="Profile not updated, Please try again"
        return render(request,'EditProfile.html',{"curl":curl,"msg":msg,'customer':listofdic[0]})

def deletebooking(request):
    
    emailid=request.session.get("emailid")
    password=request.session.get("password") 
    listofdic=Customer.objects.filter(email=emailid,password=password).values()
    print(listofdic[0])
    if request.method == "GET":
        b_id=request.GET.get('id')
        print(b_id)
        booking=Booking.objects.get(booking_id=b_id)
        msg=""
        try: 
            booking.delete()
            msg="Booking Deleted Successfully!!"
        except:
            msg="Booking Not Deleted!!"
        qs=Booking.objects.all().values()
        print(qs)    
        return render(request,'BookingDetails.html',{"curl":curl,'bookingdetails':qs,'customer':listofdic[0],"msg":msg})    
         
def changepassword(request):
    if request.method == "GET":
        emailid=request.session.get("emailid")
        password=request.session.get("password") 
        listofdic=Customer.objects.filter(email=emailid,password=password).values()
        print(listofdic[0],emailid,password)
        return render(request,'ChangePassword.html',{"curl":curl,'customer':listofdic[0]})
    elif request.method == "POST":
        emailid=request.session.get("emailid")
        password=request.session.get("password") 
        listofdic=Customer.objects.filter(email=emailid,password=password).values()
        print(listofdic[0],emailid,password)
        oldpassword = request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
        print(oldpassword,newpassword,confirmpassword)
        msg=""
        if newpassword == confirmpassword:
            Customer.objects.filter(email=emailid,password=password).update(password=confirmpassword)
            request.session["password"]=confirmpassword
            msg="Password Changed Successfully"
            emailid=request.session.get("emailid")
            password=request.session.get("password") 
            listofdic=Customer.objects.filter(email=emailid,password=password).values()
            print(listofdic[0],emailid,password)
        else:
            msg="New Password or Confirm Password not same"
    return render(request,'ChangePassword.html',{"curl":curl,"msg":msg,'customer':listofdic[0]})  


def searchhotel(request):
    emailid=request.session.get("emailid")
    password=request.session.get("password") 
    listofdic=Customer.objects.filter(email=emailid,password=password).values()
    print(listofdic[0])
    if request.method == "POST":   
       searchcity = request.POST['searchcity']
       qs=Hotel.objects.filter(hotel_city=searchcity).values()
       print(qs)
       return render(request,'CustomerHome.html',{"curl":curl,'hotel_data':qs,'customer':listofdic[0],'media_url':media_url,'msg':"Found Hotels..."})
    else:
        qs=Hotel.objects.all()
        hotel_data = qs.values()
        print(hotel_data)
        return render(request,'CustomerHome.html',{'customer':listofdic[0],'media_url':media_url,'hotel_data':hotel_data})

def Logout(request):
    logout(request)
    return redirect('http://localhost:8000/login/')

def payment(request):
    emailid=request.session.get("emailid")
    password=request.session.get("password") 
    listofdic=Customer.objects.filter(email=emailid,password=password).values()
    print(listofdic[0])

    # authorize razorpay client with API Keys.
    client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    
    data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    price=request.GET.get('price')
    return render(request,'Payment.html',{'price':price,'customer':listofdic[0]})
