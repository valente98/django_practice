from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('double/', views.double, name='double')
]
