from django.urls import path
from . import views


urlpatterns = [
    
    path('DbData',views.note)
]