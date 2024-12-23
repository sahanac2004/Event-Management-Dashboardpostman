from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event_app.views import calendar_view, index, event_management, attendee_management, task_tracker, EventViewSet, AttendeeViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'attendees', AttendeeViewSet, basename='attendee')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', index, name='landing_page'),
    path('events/manage/', event_management, name='event_management'),  # Event management page
    path('attendees/manage/', attendee_management, name='attendee_management'),  # Attendee management page
    path('tasks/manage/', task_tracker, name='task_tracker'),  # Task tracker page
    path('api/', include(router.urls)),  # Include all API routes
    path('calendar/', calendar_view, name='calendar'), 
]
