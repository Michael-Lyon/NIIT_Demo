from rest_framework import serializers
from .models import Classroom, Class, Schedule


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class_name = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ['day', 'duration', 'class_name', 'teacher']

    def get_class_name(self, obj):
        return obj.class_obj.name

    def get_teacher(self, obj):
        return obj.class_obj.teacher

    def get_duration(self, obj):
        return obj.class_obj.duration