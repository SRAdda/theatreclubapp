from django import forms
from .models import Lesson, Audition, Event


# Basic forms are already templated
# Forms can be customized

class LessonForm(forms.ModelForm):
    class Meta:
        model=Lesson
        fields='__all__'

class AuditionForm(forms.ModelForm):
    class Meta:
        model=Audition
        fields='__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'
