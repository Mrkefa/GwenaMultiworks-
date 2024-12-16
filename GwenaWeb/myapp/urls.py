
from django.contrib import admin
from django.urls import path
from myapp import views
from .import views
from django.shortcuts import render
from django.contrib.auth.views import LoginView




urlpatterns = [

    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('services/', views.services, name='services'),
    path('project/', views.project, name='project'),
    path('projects/', views.projects, name='projects'),
    path('blog1/', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),
    path('blog3/', views.blog3, name='blog3'),
    path('hire/', views.hire, name='hire'),
    path('terms/', views.terms, name='terms'),
    path('starter/', views.starter, name='starter'),
    path('order/', views.order, name='order'),
    path('assets/', views.assets, name='assets'),
    path('roads/', views.roads, name='roads'),
    path('asset2/', views.asset2, name='asset2'),
    path('asset3/', views.asset3, name='asset3'),
    path('asset4/', views.asset4, name='asset4'),
    path('construction/', views.construction, name='construction'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('chatbot/', views.chatbot, name='chatbot'),
    path("assets/", views.assets, name="assets"),
    path("my_account/", views.my_account, name="my_account"),  # My Account page for bookings
    path("edit_booking/<int:booking_id>/", views.edit_booking, name="edit_booking"),  # Edit booking page
    path("cancel_booking/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),  # Cancel booking
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("register/", views.register, name="register"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),

]
