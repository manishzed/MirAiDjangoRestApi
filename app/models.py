from django.db import models

# Create your models here.
class Session(models.Model):
    ip = models.CharField(primary_key=True, max_length=50)
    cust_name = models.CharField(max_length=20, blank=True, null=True)
    is_nickname = models.CharField(max_length=5, blank=True, null=True)
    cust_nickname = models.CharField(max_length=20, blank=True, null=True)
    cust_birthday = models.DateField(blank=True, null=True)
    cust_phone = models.CharField(max_length=20, blank=True, null=True)
    cust_is_time_for_more = models.CharField(max_length=5, blank=True, null=True)
    cust_color = models.CharField(max_length=10, blank=True, null=True)
    cust_type_of_salon = models.CharField(max_length=30, blank=True, null=True)
    is_reservation_now = models.CharField(max_length=5, blank=True, null=True)
    cust_date = models.DateField(blank=True, null=True)
    cust_service_id = models.IntegerField(blank=True, null=True)
    cust_avail_msg = models.TextField(blank=True, null=True)
    cust_avail_display_options = models.TextField(blank=True, null=True)
    cust_avail_option_list = models.TextField(blank=True, null=True)
    return_list_of_dicts = models.TextField(blank=True, null=True)
    cust_duration = models.IntegerField(blank=True, null=True)
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    return_dict = models.TextField(blank=True, null=True)
    cust_responses = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session'


class Reservations(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    sub_service_id = models.IntegerField()
    employee_ids = models.CharField(max_length=256, blank=True, null=True)
    reservation_number = models.CharField(max_length=64, blank=True, null=True)
    is_event = models.IntegerField()
    all_day = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    extra_start_date = models.DateTimeField()
    extra_end_date = models.DateTimeField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    service_start_time = models.TimeField()
    service_finish_time = models.TimeField()
    note = models.TextField(blank=True, null=True)
    event_name = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    channel = models.CharField(max_length=2048, blank=True, null=True)
    service_data = models.TextField(blank=True, null=True)
    reservation_date = models.DateField(blank=True, null=True)
    reservation_time = models.TimeField(blank=True, null=True)
    reservation_type = models.CharField(max_length=256)
    staff_name = models.TextField(blank=True, null=True)
    staff = models.CharField(max_length=2048, blank=True, null=True)
    menu = models.IntegerField()
    estimation_time = models.IntegerField(blank=True, null=True)
    coupon = models.CharField(max_length=2048, blank=True, null=True)
    reservation_total = models.CharField(max_length=256)
    used_points = models.CharField(max_length=256)
    payment_total = models.CharField(max_length=256)
    services = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    is_gmail = models.IntegerField()
    salon_board = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservations'
		
		
		
		
class Customers(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    salon_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField()
    jts_customer_code = models.CharField(max_length=256)
    hotpaper_customer_code = models.CharField(max_length=256)
    customer_code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    kana_first_name = models.TextField(blank=True, null=True)
    kana_last_name = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    kana = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    zip_code = models.TextField(blank=True, null=True)
    prefecture = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    subscription_of_news = models.TextField(blank=True, null=True)
    know_about_company = models.TextField(blank=True, null=True)
    how_did_you_come = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    is_gmail = models.IntegerField()
    salon_board = models.IntegerField()
    verification_code = models.TextField(blank=True, null=True)
    last_visited = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'
		
		
		
class SubServices(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    name = models.TextField()
    duration = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sub_services'
		
		
		
		
class Employees(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField()
    touch_id = models.TextField(blank=True, null=True)
    emp_code = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    is_technician = models.CharField(max_length=11)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    designation = models.CharField(max_length=256, blank=True, null=True)
    salary = models.CharField(max_length=256, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=256, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    role_id = models.IntegerField()
    role_title = models.CharField(max_length=256, blank=True, null=True)
    lunch_time = models.CharField(max_length=256)
    start_lunch_time = models.TimeField()
    end_lunch_time = models.TimeField()
    device_type = models.CharField(max_length=256, blank=True, null=True)
    employement_type = models.IntegerField()
    device_token = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'