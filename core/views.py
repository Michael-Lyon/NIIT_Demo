from rest_framework import viewsets
from .models import Classroom, Class, Schedule
from .serializers import ClassroomSerializer, ClassSerializer, ScheduleSerializer
from django.views.decorators.csrf import csrf_exempt

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
