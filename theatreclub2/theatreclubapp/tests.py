from django.test import TestCase
from .models import Lesson, Event, Audition
from .views import index, lessons, lessondetail, events, eventdetail, auditions, auditiondetail
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from .forms import AuditionForm, EventForm, LessonForm

# Create your tests here
class LessonTest(TestCase):
    def test_stringoutput(self):
        lesson=Lesson(lessontitle='monthly')
        self.assertEqual(str(lesson), lesson.lessontitle)

    def test_tablename(self):
        self.assertEqual(str(Lesson._meta.db_table), 'lesson')

class AuditionTest(TestCase):
    def test_stringOutput(self):
        audition=Audition(auditionname='')
        self.assertEqual(str(audition), audition.auditionname)

    def test_tablename(self):
        self.assertEqual(str(Audition._meta.db_table), 'audition')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='gala')
        self.assertEqual(str(event), event.eventtitle)

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class New_Event_Form_Test(TestCase):
    def test_UserForm_invalid(self):
        form = EventForm(data={'eventtitle': "Theme and Variations", 
        'eventlocation': "McCaw Hall", 'user': "sally", 
        'eventdate': "2019-06-01", 'eventdescription': "Pacific Northwest Ballet",
        'eventURL': "http//:www.pnb.org"})
        self.assertFalse(form.is_valid())

class TestIndex(TestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'theatreclubapp/index.html')
 