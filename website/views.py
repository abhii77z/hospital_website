from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from . models import Department, Doctor,Therapist,Blog, Appointment , Contact ,Doctordetails
from .forms import AppointmentForm , ContactForm   



# Create your views here.
def index(request):
    departments = Department.objects.all() 
    doctors = Doctor.objects.all()
    therapy = Therapist.objects.all()
    blog = Blog.objects.all()
    # Fetch all doctors from the database
    forms = AppointmentForm() 
    if request.method == "POST":
        forms = AppointmentForm(request.POST)
        if forms.is_valid():
            # Save the form data to the database
            forms.save()
            forms = AppointmentForm()  # Reset the form after saving
            return render(request , 'index.html',{'form': forms})
            return HttpResponse("Form submitted successfully!")
    
    
    
    
    
     # Create an instance of the AppointmentForm
    return render(request, 'index.html',
                  {"departments": departments, "doctors": doctors ,
                    "therapy": therapy , "blog": blog, "form": forms})  # Pass the departments and doctors to the template



# def appointment_view(request):
#     if request.method == "POST":
#         first_name = request.POST.get("first_name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         gender = request.POST.get("gender")
#         date = request.POST.get("date")
#         department = request.POST.get("department")
#         comment = request.POST.get("comment")

#         # Appointment.objects.create(
#         #     first_name=first_name,
#         #     email=email,
#         #     phone=phone,
#         #     gender=gender,
#         #     date=date,
#         #     department=department,
#         #     comment=comment
#         # )

#         return HttpResponse("Form submitted successfully!")
#     return render(request, "index.html")
def about(request):
   therapy = Therapist.objects.all()
   departments = Department.objects.all()
   return render(request, 'about.html', {'therapy': therapy ,"departments": departments })



def service(request):
    return render(request, 'service.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()  # Reset the form after saving
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()  # Create a new empty form instance
    return render(request, 'contact.html' , {'form': form})  
def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog})


def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = AppointmentForm()  # Reset the form after saving
            return render(request, 'appointment.html', {'form': form, 'success': True})
    else:
        form = AppointmentForm()  # Create a new empty form instance

    return render(request, 'appointment.html', {'form': form})
def feature(request):
    return render(request, 'feature.html')
def team(request):
    departments = Department.objects.all() 
    doctors = Doctordetails.objects.all()

    therapy = Therapist.objects.all()
    blog = Blog.objects.all()
    # Fetch all doctors from the database
    forms = AppointmentForm() 
    if request.method == "POST":
        forms = AppointmentForm(request.POST)
        if forms.is_valid():
            # Save the form data to the database
            forms.save()
            forms = AppointmentForm()  # Reset the form after saving
            return render(request , 'team.html',{'form': forms})
            return HttpResponse("Form submitted successfully!")
    
    return render(request, 'team.html',
                  {"departments": departments, "doctors": doctors ,
                    "therapy": therapy , "blog": blog, "form": forms})  # Pass the departments and doctors to the template
def testimonial(request):
    return render(request, 'testimonial.html')

def custom_404(request, exception):
    return render(request, 'custom_404.html', status=404)



def doctor_detail(request, id):
    doctor = get_object_or_404(Doctordetails, id=id)
    languages = doctor.d_languages.split(",") if doctor.d_languages else []
    return render(request, 'Doctordetails.html', {
        'doctor': doctor,
        'languages': languages
    })