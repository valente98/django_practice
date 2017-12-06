from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('double/', views.double, name='double'),
    path('multThree/', views.multThree, name='multThree'),
    path('earning/', views.earning, name='earning'),
    path('bothTrue/', views.bothTrue, name='bothTrue')
]
