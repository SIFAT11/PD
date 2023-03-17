from django.urls import path
from .views import *

urlpatterns = [
   path('',Home,name='home'),
   path('login/',log,name='login'),
   path('Reg/',reg,name='Regist'),
   path('profile/',profile,name='profile'),
   path('big/<int:id>/',showBProfile,name='BIGP'),
   path('all/',alldataa,name='ALL'),
   path('Deleteprofile/<int:id>/',Deleteprofile,name='Deleteprofile'),
   path('update/<int:id>/',update,name='update'),
]