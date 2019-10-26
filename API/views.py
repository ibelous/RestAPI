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


class LectureList(generics.ListAPIView):
    serializer_class = LectureSerializer

    def get_queryset(self):
        return Lecture.objects.filter(course_id=self.kwargs['course_id'])


class LectureCreate(generics.CreateAPIView):
    lookup_url_kwarg = 'course_id'
    serializer_class = LectureSerializer
    queryset = Lecture.objects.all()
    permission_classes = [TeacherPermissions]


class LectureRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LectureSerializer
    lookup_url_kwarg = 'lecture_id'

    def get_queryset(self):
        return Lecture.objects.filter(course_id=self.kwargs['course_id'])


class HomeTaskCreate(generics.CreateAPIView):
    serializer_class = HomeTaskSerializer
    queryset = HomeTask.objects.all()
    permission_classes = [TeacherPermissions]


class HomeTaskList(generics.ListAPIView):
    serializer_class = HomeTaskSerializer
    lookup_url_kwarg = 'lecture_id'
    queryset = HomeTask.objects.all()


class HomeTaskRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HomeTaskSerializer
    lookup_url_kwarg = 'hometask_id'

    def get_queryset(self):
        return HomeTask.objects.all()


class HomeWorkCreate(generics.CreateAPIView):
    serializer_class = HomeWorkSerializer
    queryset = HomeWork.objects.all()


class HomeWorkList(generics.ListAPIView):
    serializer_class = HomeWorkSerializer
    queryset = HomeWork.objects.all()


class HomeWorkRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HomeWorkSerializer
    lookup_url_kwarg = 'homework_id'

    def get_queryset(self):
        return HomeWork.objects.all()


class HomeWorkRateRU(generics.RetrieveUpdateAPIView):
    serializer_class = RateSerializer
    lookup_url_kwarg = 'homework_id'
    queryset = WorkRate.objects.all()
