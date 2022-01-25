from django.urls import path
from .import views
from django.contrib import admin



urlpatterns = [
    path('home',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('complain/',views.complain,name='complain'),
    path('event/',views.event,name='event'),
    path('note/',views.note,name='note'),
    path('logout/',views.logout,name='logout'),
    path('profiles/',views.profiles,name='profiles'),
    path('',views.login,name='login'),
    path('payment/paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('payment/', views.payment, name='payment'),
   


]