from django.urls import path
# from .views import Index
from . import views

urlpatterns = [
    # path('', Index),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('school_admin/', views.school_admin, name='school_admin'),
]