from django.http import HttpResponse
from django.shortcuts import render,redirect
# from hotelbooking.form import UserLogin,UserRegister
from django.conf import settings
from hotelbooking.models import Customer

curl = settings.BASE_URL

def index(request):
    return render(request,'index.html',{"curl":curl})
   
def about(request):
    return render(request,'about.html',{"curl":curl})

def register(request):
    if request.method == "GET":
        return render(request,'register.html',{"curl":curl})
    
    elif request.method == "POST":
        print("====================POST")
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        address = request.POST['address']
        gender = request.POST['gender']
        dob = request.POST['dob']
        print(name,email,password,mobile,address,dob,gender)
        customer = Customer(name=name,email=email,password=password,mobile=mobile,address=address,gender=gender,dob=dob)
        msg=""
        try:
            customer.save()
            msg="Customer Register Successfully"
        except Exception as e:
            print("Error Occured at Register Customer:",e)
            msg="Customer Not Register, Please try again"
        return render(request,'register.html',{"curl":curl,"msg":msg})

'''
def login(request):
    fm = UserLogin()
    msg=""
    if request.method == "POST":
        fm = UserLogin(request.POST)  
        if fm.is_valid():
            print("Form Validated")
            print("Email:",fm.cleaned_data['email'])
            print("Password:",fm.cleaned_data['password'])       
        else:
            print(" Not Validated ============")
            return render(request,'login.html',{'form':fm,'msg':msg,'curl':curl}) 
            
    elif request.method == "GET":
        print("get request")
        return render(request,'login.html',{'form':fm,'curl':curl})  
'''
# Django Form
'''  
def register(request):
    fm=UserRegister()
    if request.method == "POST":
        fm=UserRegister(request.POST)
        if fm.is_valid():
        #    name=fm.cleaned_data['name']
           email=fm.cleaned_data['email']
           password=fm.cleaned_data['password']
        #    gender=fm.cleaned_data['gender']
        #    dob=fm.cleaned_data['dob']
        #    mobile=fm.cleaned_data['mobile']
        #    print(name,email,password,gender,dob,mobile)
           return render(request,'register.html',{"curl":curl,'msg':"Get Data Successfully!!"})
        else:
            return render(request,'register.html',{"curl":curl,'form':fm})
        
    elif request.method == "GET":
        return render(request,'register.html',{"curl":curl,'form':fm})
'''

def login(request):
    if request.method == "GET":
        return render(request,'login.html',{"curl":curl})
    elif request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        qset = Customer.objects.filter(email=email,password=password).values()
        # print(qset)
        msg=""
        if not qset:
            msg="Please enter correct email or password"
            return render(request,'login.html',{"curl":curl,'msg':msg})  
        else:
            print(qset[0]["role"])
            role = qset[0]["role"]
            if role == "customer":
                return redirect(curl+'/customer/home')
            elif role == "admin":
                return redirect(curl+'/hoteladmin/home')
    else:
        return render(request,'login.html',{"curl":curl,'msg':msg})        
