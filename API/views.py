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
    permission_classes = (TeacherPermissionsOrReadOnly,)


class CourseRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsMember, TeacherPermissionsOrReadOnly]
    lookup_url_kwarg = 'course_id'

    def get_queryset(self):
        return Course.objects.filter(users__id=self.request.user.id)


class LectureList(generics.ListAPIView):
    serializer_class = LectureSerializer
    permission_classes = [IsMember]

    def get_queryset(self):
        return Lecture.objects.filter(course_id=self.kwargs['course_id'])


class LectureCreate(generics.CreateAPIView):
    serializer_class = LectureSerializer
    permission_classes = [TeacherPermissionsOrReadOnly, IsMember]
    queryset = Lecture.objects.all()


class LectureRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LectureRUDSerializer
    # lookup_url_kwarg = 'lecture_id'
    permission_classes = [TeacherPermissionsOrReadOnly, IsMember]

    def get_queryset(self):
        return Lecture.objects.filter(course_id=self.kwargs['course_id'])


class HomeTaskCreate(generics.CreateAPIView):
    serializer_class = HomeTaskSerializer
    queryset = HomeTask.objects.all()
    permission_classes = [TeacherPermissionsOrReadOnly, IsMember]


class HomeTaskList(generics.ListAPIView):
    serializer_class = HomeTaskSerializer
    # lookup_url_kwarg = 'hometask_id'
    permission_classes = [IsMember]

    def get_queryset(self):
        return HomeTask.objects.filter(lecture__course_id=self.kwargs['course_id'],
                                       lecture_id=self.kwargs['lecture_id'])


class HomeWorkCreate(generics.CreateAPIView):
    serializer_class = HomeWorkSerializer
    queryset = HomeWork.objects.all()
    permission_classes = [IsMember]


class HomeWorkRU(generics.RetrieveUpdateAPIView):
    serializer_class = HomeWorkSerializer
    permission_classes = [IsMember, MyHomeWork]
    lookup_url_kwarg = 'homework_id'

    def get_queryset(self):
        return HomeWork.objects.filter(task_id=self.kwargs['hometask_id'])


class HomeWorkList(generics.ListAPIView):
    serializer_class = HomeWorkSerializer
    permission_classes = [IsMember]

    def get_queryset(self):
        return HomeWork.objects.filter(task_id=self.kwargs['hometask_id'], student=self.request.user)


class AllHomeWorkList(generics.ListAPIView):
    serializer_class = HomeWorkSerializer
    permission_classes = [IsMember, TeacherPermissions]

    def get_queryset(self):
        return HomeWork.objects.filter(task_id=self.kwargs['hometask_id'])


class HomeWorkRateCreate(generics.CreateAPIView):
    serializer_class = RateSerializer
    lookup_url_kwarg = 'homework_id'
    queryset = WorkRate.objects.all()
    permission_classes = [IsMember, TeacherPermissionsOrReadOnly, MyHomeWork]


class HomeWorkRateR(generics.ListAPIView):
    serializer_class = RateSerializer
    lookup_url_kwarg = 'homework_id'
    permission_classes = [IsMember, MyHomeWork]

    def get_queryset(self):
        return WorkRate.objects.filter(work=HomeWork.objects.get(id=self.kwargs['homework_id']))


class CommentCreate(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsMember, MyHomeWork]
    lookup_url_kwarg = 'homework_id'

    def get_queryset(self):
        return RateComment.objects.all()


class CommentList(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsMember, MyHomeWork]
    # lookup_url_kwarg = 'homework_id'

    def get_queryset(self):
        return RateComment.objects.filter(rate=HomeWork.objects.get(id=self.kwargs['homework_id']).rate)
