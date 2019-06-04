from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lesson(models.Model):
    lessontitle=models.CharField(max_length=255)
    lessondate=models.DateField(auto_now=False,auto_now_add=False)
    lessontime=models.TimeField(auto_now=False,auto_now_add=False)
    location=models.TextField()
    agenda=models.TextField()
    
    def __str__(self): 
        return self.lessontitle
        
    class Meta:
        db_table='lesson'
        verbose_name_plural='lessons'

class Audition(models.Model):
    auditionname=models.CharField(max_length=255)
    auditiontype=models.CharField(max_length=255)
    auditionURL=models.URLField(null=True, blank=True)
    entryDate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    auditiondescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.auditionname
        
    class Meta:
        db_table='audition'
        verbose_name_plural='auditions'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField()
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField(null=True, blank=True)
    eventURL=models.URLField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self): 
        return self.eventtitle
        
    class Meta:
        db_table='event'
        verbose_name_plural='events'
