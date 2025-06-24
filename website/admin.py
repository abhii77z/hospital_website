from django.contrib import admin

# Register your models here.
from .models import Department , Doctor ,Therapist,Blog ,Appointment, Contact, Doctordetails  

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dep_name', 'dep_description')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_department', 'doc_image') 


class TherapyAdmin(admin.ModelAdmin):
    list_display = ('th_name','th_des','th_img')  

class BlogAdmin(admin.ModelAdmin):
    list_display = ('b_name', 'b_date', 'b_comment', 'b_image' , 'b_button' , 'b_con') 


class AppointmentAdmin(admin.ModelAdmin):  # ✅ new admin class for Appointment
    list_display = ('first_name', 'email', 'phone', 'gender', 'date', 'department', 'comment')   

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'project', 'message', 'subject')

class DoctordetailAdmin(admin.ModelAdmin):
    list_display = ('d_name', 'd_department', 'd_image', 'd_description', 
                    'd_age', 'd_experience', 'd_qualification', 'd_profsummary', 
                    'd_email', 'd_phone', 'd_languages', 'd_education', 'd_awards')  # ✅ Add this line to display doctor details


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Therapist, TherapyAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Appointment, AppointmentAdmin)  # ✅ register the Appointment model
admin.site.register(Contact, ContactAdmin)  # ✅ register the Contact model
admin.site.register(Doctordetails, DoctordetailAdmin)  # ✅ register the Doctordetails model
