from django.urls import path
from . import views
# from .views import appointment_view
urlpatterns = [
    path('', views.index, name='index'),
    # Add more URL patterns as needed
    # path('appointment/', appointment_view, name='appointment')
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('appointment/', views.appointment, name='appointment'),
    path('feature/', views.feature, name='feature'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('custom_404/', views.custom_404, name='custom_404'),
    path('doctor/<int:id>/', views.doctor_detail, name='doctor_detail'),

]