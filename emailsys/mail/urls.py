from django.urls import path
from mail import views

urlpatterns = [
    path('', views.mail, name='main'),
    path('newmail',views.get_mail,name='mail'),
    path('sendmail',views.end_mail,name='smail')
]