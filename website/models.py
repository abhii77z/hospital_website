from django.db import models

# Create your models here.
class Department (models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    def __str__(self):
        return self.dep_name
    




class Doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors/')
    
    # Link to detailed profile
    detail = models.ForeignKey('Doctordetails', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.doc_name
    

    

class Therapist(models.Model):
    th_name = models.CharField(max_length=30)    
    th_des = models.CharField(max_length=200)
    th_img = models.ImageField(upload_to='Therapy/', null=True, blank=True)
    def __str__(self):
        return self.th_name
    

class Blog(models.Model):
    b_name = models.CharField(max_length=100)
    b_date = models.DateField(auto_now_add=True)
    b_comment = models.TextField(max_length=200)
    b_image = models.ImageField(upload_to='blog/')
    b_con = models.TextField(max_length=2500, default='ok')  # ✅ Add this
    b_button = models.CharField(max_length=100, default='Read More')  # ✅ Add this

    def __str__(self):
        return self.b_name
    
 
    

class Appointment(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]   
    DOCTOR_CHOICES =[
        Doctor.doc_name
    ]
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES )
    date = models.DateField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)


    comment = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.first_name} - {self.date}"    
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    project = models.CharField(max_length=100)
    message = models.TextField()
    subject = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} - {self.project}"
    


class Doctordetails(models.Model):       
    d_name = models.CharField(max_length=100)
    d_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    d_image = models.ImageField(upload_to='doctors/')
    d_description = models.TextField()
    d_age = models.IntegerField()
    d_experience = models.IntegerField()
    d_qualification = models.CharField(max_length=200)
    d_profsummary = models.TextField()
    d_email = models.EmailField()
    d_phone = models.CharField(max_length=15)
    d_languages = models.CharField(max_length=200)
    d_education = models.TextField()
    d_awards = models.TextField()
    
    def __str__(self):
        return self.d_name


