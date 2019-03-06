from django.urls import path
from . import views
from .views import home,car_page,login

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('career',views.car_page,name='car_page'),
    path('contact_us',views.contact,name='contact'),
    # path('api/data',views.EmailList.as_view()),
    
]