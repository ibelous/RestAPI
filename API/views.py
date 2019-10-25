from .serializers import *
from rest_framework import generics
from rest_framework.permissions import *
from .api_permissions import *


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(users__id=self.request.user.id)


class CourseCreate(generics.CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [TeacherPermissions]


class CourseRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    lookup_url_kwarg = 'course_id'

    def get_queryset(self):
        return Course.objects.filter(users__id=self.request.user.id)


class LectureCreate(generics.CreateAPIView):
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = [TeacherPermissions]


class HomeTaskCreate(generics.CreateAPIView):
    serializer_class = HomeTasks
    queryset = HomeTasks.objects.all()
    permission_classes = [TeacherPermissions]


class HomeWorkCreate(generics.CreateAPIView):
    serializer_class = HomeWorkSerializer
    queryset = HomeWork.objects.all()


class HomeWorkRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HomeWorkSerializer
    queryset = HomeWork.objects.all()
