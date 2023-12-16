from django.contrib import admin
from .models import CustomerProfile, BackboneCustomerInfo, User, Showroom, BackboneCustomerEvent

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']
    
@admin.register(BackboneCustomerInfo)
class BackboneCustomerInfoAdmin(admin.ModelAdmin):
    list_display = ['id','appointment_type','appointment_time','stage']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','customer_profile_id']
    
@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    list_display = ['supplier_id']
    
@admin.register(BackboneCustomerEvent)
class BackboneCustomerEvent(admin.ModelAdmin):
    list_display = ['cust_id','showroom_id']