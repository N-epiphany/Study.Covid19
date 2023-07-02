from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('india/', views.india, name='india'),
    path('india/state/', views.state_analysis_view, name='state'),
    path('india/district/', views.district_analysis_view, name='district'),
    path('world/', views.world, name='world'),
    path('contact/', views.contact, name='contact'),
]
