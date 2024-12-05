from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.guest, name='home'),
    path('reservation/', views.reservation, name='reservation'),
    path('postguest/', views.postguest, name="postguest"),
    path('postreservation/', views.postreservation, name='postreservation'),
]
