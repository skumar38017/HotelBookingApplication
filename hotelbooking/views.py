from django.http import HttpResponse
from django.shortcuts import render,redirect
# from hotelbooking.form import UserLogin,UserRegister
from django.conf import settings
from hotelbooking.models import Customer
from . import emailSending
import uuid
from .helpers import send_forget_mail

curl = settings.BASE_URL

def index(request):
    return render(request,'index.html',{"curl":curl})
   
def about(request):
    return render(request,'about.html',{"curl":curl})

def changepassword(request,token):
    cust_obj=Customer.objects.filter(forgot_password_token=token).first()
    print(cust_obj.customer_id)

    if request.method == 'POST':
        newpassword=request.POST.get('newpassword')
        confirmpassword=request.POST.get('confirmpassword')
        c_id=request.POST.get('customer_id')
        if c_id is None:
           print("No User Id Found")
           return redirect(curl+'/changepassword/'+token)
       
        if newpassword != confirmpassword:
           print("newpassword and confirmpassword is not same")
           return redirect(curl+'/changepassword/'+token)
        
        Customer.objects.filter(customer_id=c_id).update(password=confirmpassword)
        print("Password Reset Successfully")
        # return redirect(curl+"/login/")
        return render(request,'login.html',{"curl":curl,"msg":"Password Reset Successfully"})
    else:
        return render(request,'email.html',{"curl":curl,"customer_id":cust_obj.customer_id})

def forgotpassword(request):
    if request.method == 'POST':
        email=request.POST.get('email')
 
        if not Customer.objects.filter(email=email).first():
            print("No User Found with this email")
            return redirect(request,curl+'/forgotpassword/')
            
        cust_obj = Customer.objects.filter(email=email).first()
        print(type(cust_obj),cust_obj.email)
        token = str(uuid.uuid4())
        #===== Save token ====#
        cust = Customer.objects.get(email=cust_obj.email)
        cust.forgot_password_token = token
        cust.save()
        #=========Save token =====#
        send_forget_mail(cust_obj.email,token)
        print("Email is send to your gmail id")
        return render(request,'forgotpassword.html',{"curl":curl})
    return render(request,'forgotpassword.html',{"curl":curl})

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
            # for send verification email to registered email id
            emailSending.sendMail(email, password)
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
        listdic = qset.values()
        msg=""
        if not qset:
            msg="Please enter correct email or password"
            return render(request,'login.html',{"curl":curl,'msg':msg})  
        else:
             #for session ============================
            request.session["emailid"]=listdic[0]["email"]
            request.session["password"]=listdic[0]["password"]
            request.session["role"]=listdic[0]["role"]
            request.session["customer_id"]=listdic[0]["customer_id"]
            print(qset[0]["role"])
            role = qset[0]["role"]
            if role == "customer":
                return redirect(curl+'/customer/home')
            elif role == "admin":
                return redirect(curl+'/hoteladmin/home')
    else:
        return render(request,'login.html',{"curl":curl,'msg':msg})        
