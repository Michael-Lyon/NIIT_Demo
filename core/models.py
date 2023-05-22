from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.duration}: {self.teacher}: {self.classroom}"


class Schedule(models.Model):
    DAY_CHOICES = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )
    TIME_CHOICES = (
        ('9-11', '9-11'),
        ('11-1', '1-3'),
        ('1-3', '3-5'),
    )
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    duration = models.CharField(max_length=7, choices=TIME_CHOICES)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day}: {self.duration}: {self.class_obj}"
