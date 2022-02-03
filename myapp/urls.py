from django.urls import path
from .import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('sign-up/',views.signup,name='sign-up'),
    path('profile/',views.profile,name='profile'),
    path ('notifications/',views.notifications,name='notifications'),
    path ('dashboard/',views.dashboard,name='dashboard'),
    path ('otp/',views.otp,name='otp'),
    path ('',views.signin,name='sign-in'),
    path('logout/',views.logout,name='logout'),
    path('Forgot-Password/',views.ForgotPassword,name='Forgot Password'),
    path('emergency-contact/',views.emergency_contact,name='emergencycontact'),
    path('com/',views.com,name='com'),
    path('event gallery/',views.eventgallery,name='event gallery'),
    path('societymemberinfo/',views.societymemberinfo,name='societymemberinfo'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('deletes/<int:pk>',views.deletes,name='deletes'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('deletess/<int:pk>',views.deletess,name='deletess'),

] 