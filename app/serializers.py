from rest_framework import serializers
from .models import Session
from .models import Reservations
from .models import Customers
from .models import SubServices
from .models import Employees

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ("ip", "cust_name","is_nickname","cust_nickname","cust_birthday","cust_phone"," cust_is_time_for_more","cust_color","cust_type_of_salon","is_reservation_now","cust_date","cust_service_id","cust_avail_msg","cust_avail_display_options ","cust_avail_option_list","return_list_of_dicts ","cust_duration","state","return_dict ","cust_responses")


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = (" user_id","customer_id ","service_id","sub_service_id","employee_ids","reservation_number","is_event","all_day","start_date","end_date","extra_start_date","extra_end_date","start_time ","end_time","service_start_time","service_finish_time","note","event_name","name ","channel","service_data","reservation_date ","reservation_time","reservation_type"," staff_name","staff","menu","estimation_time","coupon","reservation_total ","used_points","payment_total","services","services","status ","is_gmail","salon_board","created ","modified")
		
class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ("user_id","salon_id ","service_id","jts_customer_code","hotpaper_customer_code","customer_code","name","kana_first_name ","kana_last_name","first_name","last_name","email","kana","gender","dob","age","tel","zip_code","prefecture","city ","address1","address2","job","subscription_of_news","know_about_company","how_did_you_come","status ","is_gmail","salon_board","  verification_code","last_visited","created"," modified")
		
		
class SubServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubServices
        fields = ("user_id","service_id","name","duration","price","status","created","modified")
		
		
		
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (" user_id","service_id"," touch_id","emp_code","name","email","is_technician","dob","phone","joining_date","designation","salary","address","image","status","role_id","role_status","lunch_time"," start_lunch_time"," end_lunch_time","device_type","employement_type","device_token","created"," modified")\
