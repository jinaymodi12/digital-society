from django.shortcuts import render
from myapp import models as m
from .models import *
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# Create your views here.
def home(request):
    try:
        uid=User.objects.get(email=request.session['emails'])
        return render(request,'home.html',{'uid':uid}) 
    except:
        return render(request,'home.html') 


def contact(request):
    v=m.Emergency_Contact.objects.all()	
	
    return render(request,'contact.html',{'v':v})   

def about(request):
    return render(request,'about.html')   

def complain(request):
    msg='YOUR COMPLAIN SEND SUCCESSFULLY'
    if request.method=='POST':
        name=request.POST['name']
        flat=request.POST['flat']
        mobile=request.POST['mobile']
        description=request.POST['description']
        Complain.objects.create(name=name,flat=flat,mobile=mobile,description=description)
        return render(request,'complain.html',{'msg':msg})
    else:
        msg='ERROR'
        return render(request,'complain.html',{'msg':msg})
def event(request):
    q=m.Event_gallery.objects.all()[::-1]
    return render(request,'event.html',{'q':q})

def note(request):
    s=m.Notifications.objects.all()[::-1]
    return render(request,'note.html',{'s':s})

def logout(request):
    del request.session['emails']
    return render(request,'login.html')


def profiles(request):
    msg='PROFILE UPDATE SUCCESSFULLY'
    uid=User.objects.get(email=request.session['emails'])
    if request.method=='POST':
        uid.name = request.POST['name']
        uid.mail = request.POST['email']
        uid.mobile = request.POST['mobile']
        uid.address=request.POST['address']
        uid.password=request.POST['password']
        uid.save()
        return render(request,'profiles.html',{'msg':msg,'uid':uid})
    else:
        return render(request,'profiles.html',{'uid':uid})

def login(request):
     if request.method=='POST':
        try:
            uid=User.objects.get(email=request.POST['email'])
            if request.POST['password']== uid.password:
                request.session['emails']=request.POST['email']
                print(request.session['emails'])
                return render(request,'home.html',{'uid':uid})
            else:
                return render(request,'login.html',{'msg':'INVALID DATA'})
        except:
            msg='GO AND SIGNUP FIRST'
            return render(request,'login.html',{'msg':msg})
     return render(request,'login.html')






# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def payment(request):
	global temp
	uid = User.objects.get(email=request.session['emails'])
	temp={
		'uid':uid 
	}
	currency = 'INR'
	amount = 20000 # Rs. 200
	

	# Create a Razorpay Order
	razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
	razorpay_order_id = razorpay_order['id']
	callback_url = 'paymenthandler/'

	# we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = razorpay_order_id
	context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['callback_url'] = callback_url
	context['uid'] = uid

	return render(request, 'payment.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is None:
                amount = 20000  # Rs. 200
                try:
					
                    # capture the payemt

                    razorpay_client.payment.capture(payment_id, amount)
                    # render success page on successful caputre of payment
				#	return render(request, 'paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
			#else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()