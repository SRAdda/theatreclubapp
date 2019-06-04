from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Lesson, Audition, Event
from django.http import HttpResponseNotModified
from .forms import LessonForm, AuditionForm, EventForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'theatreclubapp/index.html')

def lessons(request):
    lessons_list=Lesson.objects.all()
    return render(request, 'theatreclubapp/lessons.html' , {'lessons_list': lessons_list})

def lessondetail(request, id):
    lessondetail=get_object_or_404(Lesson, pk=id)
    return render(request, 'theatreclubapp/lessondetail.html', {'lesson' : lesson})

def events(request):
    events_list=Event.objects.all()
    return render(request, 'theatreclubapp/events.html', {'events_list': events_list})    

def eventdetail(request, id):
    event=get_object_or_404(Event, pk=id)
    return render(request, 'theatreclubapp/eventdetail.html', {'event' : event})

def auditions(request):
    auditions_list=Audition.objects.all()
    return render(request, 'theatreclubapp/auditions.html', {'auditions_list': auditions_list})

def auditiondetail(request, id):
    audition=get_object_or_404(Audition, pk=id)
    return render(request, 'theatreclubapp/auditiondetail.html', {'audition' : audition})

def newLesson(request):
    form=LessonForm
    if request.method=='POST':
        form=LessonForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=LessonForm()

    else:
        form=LessonForm()
    return render(request, 'theatreclubapp/newlesson.html', {'form': form})

def newAudition(request):
    form=AuditionForm
    if request.method=='POST':
        form=AuditionForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=AuditionForm()

    else:
        form=AuditionForm()
    return render(request, 'theatreclubapp/newaudition.html', {'form': form})

def newEvent(request):
    form=EventForm
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()

    else:
        form=EventForm()
    return render(request, 'theatreclubapp/newevent.html', {'form': form})

def loginmessage(request):
    return render(request, 'theatreclubapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'theatreclubapp/logoutmessage.html')
