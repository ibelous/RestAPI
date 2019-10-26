from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'teacher'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)

    def __str__(self):
        return self.username


class Course(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures')
    topic = models.CharField(max_length=32)
    presentation = models.FileField(upload_to='presentations')
    # hometask = models.TextField(max_length=2048)

    def __str__(self):
        return self.topic


class HomeTask(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='hometasks')
    text = models.TextField(max_length=2048)


class HomeWork(models.Model):
    task = models.ForeignKey(HomeTask, on_delete=models.CASCADE, related_name='homeworks')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homeworks')
    work = models.FileField(upload_to='homeworks')


class WorkRate(models.Model):
    work = models.OneToOneField(HomeWork, on_delete=models.CASCADE, related_name='rate')
    rate = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.rate


class RateComment(models.Model):
    rate = models.ForeignKey(WorkRate, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024)
