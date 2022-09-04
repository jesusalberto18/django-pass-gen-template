from django.contrib import admin
from django.urls import path
from genapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home')
    path('about/', views.about, name='about'),
    path('generate/', views.generate, name='generate')
    path('password/', views.password, name='password')
]
