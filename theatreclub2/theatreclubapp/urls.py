from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='index'),
    path('lessons/', views.lessons, name='lessons'),
    path('lessondetail/<int:id>', views.lessondetail, name='lessondetail'),
    path('events/', views.events, name='events'),
    path('eventdetail/<int:id>', views.eventdetail, name='eventdetail'),
    path('auditions/', views.auditions, name='auditions'),
    path('auditiondetail/<int:id>', views.auditiondetail, name='auditiondetail'),
    path('newLesson/', views.newLesson, name='newlesson'),
    path('newAudition/', views.newAudition, name='newaudition'),
    path('newEvent/', views.newEvent, name='newevent'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]
