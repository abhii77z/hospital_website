from django import forms
from .models import Appointment
from . models import Contact
from django.forms import TextInput, EmailInput, Select, DateInput, Textarea

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'email', 'phone', 'gender', 'date', 'department', 'comment']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "First Name",
                'style': "background-color: #ffffff; color: #000000;"
            }),
            'email': EmailInput(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Email",
                'style': "background-color: #ffffff; color: #000000;"
            }),
            'phone': TextInput(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Phone",
                'style': "background-color: #ffffff; color: #000000;"
            }),
            'gender': Select(attrs={
                'class': "form-control py-3 border-primary",
                'style': "background-color: #ffffff; color: #000000;"
            }),
            'date': DateInput(attrs={
                'type': "date",
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Date",
                'style': "background-color: #ffffff; color: #000000;"
            }),
            'department': Select(attrs={
                'class': "form-control py-3 border-primary",
                'style': "background-color: #ffffff; color: #000000;"
            }),
            'comment': Textarea(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Comment",
                'style': "background-color: #ffffff; color: #000000;"
            }),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'project', 'message', 'subject']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Name",
                'style': "background-color: #ffffff; color: #000000; border: 1px solid #ced4da;"

            }),
            'email': EmailInput(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Email",
                'style': "background-color: #ffffff; color: #000000; border: 1px solid #ced4da;"
            }),
            'phone': TextInput(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Phone",
                'style': "background-color: #ffffff; color: #000000; border: 1px solid #ced4da;"
            }),
            'project': TextInput(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Project",
                'style': "background-color: #ffffff; color: #000000; border: 1px solid #ced4da;"
            }),
            'message': Textarea(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Message",
                'style': "background-color: #ffffff; color: #000000; border: 1px solid #ced4da;"
            }),
            'subject': TextInput(attrs={
                'class': "form-control py-3 border-primary bg-transparent text-white",
                'placeholder': "Subject",
                'style': "background-color: #ffffff; color: #000000; border: 1px solid #ced4da;"
            }),
        }