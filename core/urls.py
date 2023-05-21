from rest_framework import routers
from core.views import ClassroomViewSet, ClassViewSet, ScheduleViewSet
from django.urls import path, include

app_name="core"

router = routers.DefaultRouter()
router.register('classrooms', ClassroomViewSet)
router.register('classes', ClassViewSet)
router.register('schedules', ScheduleViewSet)

urlpatterns = [
    path("", include(router.urls))
]
