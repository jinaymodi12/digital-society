from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(user)
#@admin.register(User)
#class UserAdmin(admin.ModelAdmin):

 #   list_display = ['fname','email']
admin.site.register(Emergency_Contact)
admin.site.register(Event_gallery)
admin.site.register(Society_members_information_management)
admin.site.register(Notifications)

