from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from random import *
from django.conf import settings
from django.core.mail import send_mail
from memberapp.models import Complain as co

# Create your views here.
def index(request):
    
    return render (request,'index.html')

def signup(request):
    if request.method=='POST':
        try:
            user.objects.get(email=request.POST['email'])
            msg= 'YOUR EMAIL ALREADY EXIST'
            return render(request,'sign-up.html',{'msg':msg})
        except:
            global temp
            otp=randrange(1000,9999)

            temp={
                'fname':request.POST['name'],
                'email':request.POST['email'],
                'mobile':request.POST['mobile'],
                'address':request.POST['address'],
                'password':request.POST['password'],
            
            }

            subject='SOCIETY OTP VERIFY'
            message=f'YOUR OTP IS : {otp}'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[request.POST['email'],]
            send_mail(subject,message,email_from,recipient_list)
            return render(request,'otp.html',{'otp':otp})
    return render(request,'sign-up.html')
   # else:


#def profile(request):
 #   return render (request,'profile.html')

def notifications(request):
    try:
        msg='NOTIFICATION SEND TO ALL USERS SUCCESSFULLY'
        if request.method=='POST':
            name=request.POST['name']
            date=request.POST['date']
            disc=request.POST['disc']
            Notifications.objects.create(name=name,date=date,disc=disc)
            return render(request,'notifications.html')
        else:
            return render(request,'notifications.html')


    except:    
        return render(request,'notifications.html',{'msg':msg})
     
        

    

def dashboard(request):
    return render (request,'index.html')

def otp(request):
    if request.method == 'POST':
        if request.POST['otp'] == request.POST['sysotp']:

            global temp

            user.objects.create(

               fname = temp['fname'],
               email = temp['email'],
               mobile = temp['mobile'],
               address =temp['address'],
               password =temp['password'],
            )
            msg='user created'
            del temp
            return render(request,'sign-up.html',{'msg':msg})
    
        else:
            msg='YOUR OTP DOES NOT MATCH'
            return render(request,'otp.html',{'msg':msg,'otp':request.POST['otp']})
    return render(request,'otp.html')

def signin(request):
    if request.method=='POST':
        try:
            uid=user.objects.get(email=request.POST['email'])
            if request.POST['password']== uid.password:
                request.session['email']=request.POST['email']
                print(request.session['email'])
                return render(request,'index.html',{'uid':uid})
            else:
                return render(request,'sign-in.html',{'msg':'INVALID DATA'})
        except:
            msg='GO AND SIGNUP FIRST'
            return render(request,'sign-in.html',{'msg':msg})
    return render(request,'sign-in.html')

def logout(request):
    del request.session['email']
    return render(request,'sign-in.html')

def ForgotPassword(request):
    if request.POST:
        try:
            uid=user.objects.get(email=request.POST['email'])
            s = 'QWERTYUIOPLKJHGFDSAqwertyuioplkjhgfdsa1236547889'
            pw = ''.join(choices(s,k=8))
            subject= 'SOCIETY RESET PASSWORD'
            message = f"""Hello {uid.fname},
            Your New Password is : {pw}

              **Please Login with New Password"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            uid.password = pw
            uid.save()
            return render(request,'sign-in.html',{'msg':'New password is sent on your email'})
        except:
           return render(request,'Forgot Password.html',{'msg':'YOUR EMAIL IS NOT REGISTER'})
    return render(request,'Forgot Password.html')

def profile(request):

    uid = user.objects.get(email=request.session['email'])
    msg='YOUR PROFILE UPDATED'
    if request.method =='POST':
        uid.fname = request.POST['name']
        uid.email = request.POST['email']
        uid.mobile = request.POST['mobile']
        uid.address=request.POST['address']
        uid.password=request.POST['password']
        uid.save()
        return render(request,'profile.html',{'msg':msg,'uid':uid})
    else:
        return render(request,'profile.html',{'uid':uid})

def emergencycontact(request):
    uid=user.objects.get(email=request.session['email'])
    msg='YOUR DETAIL IS SAVE SUCCESSFULLY'
    if request.method =='POST':
        name =  request.POST['name']
        mobile = request.POST['mobile']
        occupation = request.POST['occupation']
        cont = Emergency_Contact.objects.create(name=name,mobile=mobile,occupation=occupation)
        xy=cont.save()   
        return render(request,'emergency contact.html',{'msg':msg},{'uid':uid})
    
    else:
        return render(request,'emergency contact.html')


def com(request):
  r=co.objects.all()
  reversed(r)
  return render(request,'com.html',{'r':r})

def eventgallery(request):
    msg='PICTURE UPLOAD SUCCESSFULLY'
    if request.method=='POST':
        name=request.POST['name']
        date=request.POST['date']
        disc=request.POST['disc']
        pics=request.POST['pics']
        x=Society_problem.objects.create(name=name,date=date,disc=disc,pics=pics)
        y=x.save()
        return render(request,'event gallery.html',{'msg':msg})
    else:
        return render(request,'event gallery.html')

def societymemberinfo(request):
    msg='DATA SAVED SUCCESSFULLY'
    if request.method=='POST':
        flatno=request.POST['flatno']
        member=request.POST['member']
        numberofmember=request.POST['numberofmember']
        mobile=request.POST['mobile']
        email=request.POST['email']
        Society_members_information_management.objects.create(
        flatno=flatno,
        member=member,
        numberofmember=numberofmember,
        mobile=mobile,
        email=email)
        
        return render(request,'societymemberinfo.html',{'msg':msg})
    else:
        return render(request,'societymemberinfo.html')




def delete(request,pk ):
    v=co.objects.get(id=pk)
    v.delete()
    return render(request,'com.html',{'v':v})











            