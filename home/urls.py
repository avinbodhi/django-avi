from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('visitdata/<pk>', views.visit_details, name='visit_details_api'),
    path('visitall/', views.visit_list, name='visit_list_api'),
    path('list/', views.VisitHomePage, name='VisitData'),

]
