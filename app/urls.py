from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('double/', views.double, name='double'),
    path('multThree/', views.multThree, name='multThree'),
    path('earning/', views.earning, name='earning'),
    path('bothTrue/', views.bothTrue, name='bothTrue'),
    path('WalkorDrive/', views.WalkorDrive, name='WalkorDrive'),
    path('howPopulated/', views.howPopulated, name='howPopulated'),
    path('goldStar/', views.goldStar, name='goldStar'),
    path('howManyPoints/', views.howManyPoints, name='howManyPoints'),
    path('lastThree/', views.lastThree, name='lastThree'),
    path('sumofList/', views.SumofList, name='sumofList'),
    path('sumofLonger/', views.SumofLonger, name='sumofLonger'),
    path('diffFromMin/', views.differenceFromMinimum, name="diffFromMin"),
    path('hashTags/', views.hashTags, name='hashTags'),
    path('mentions/', views.mentions, name='mentions')
]
