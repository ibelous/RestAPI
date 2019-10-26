from rest_framework import serializers
from .models import User, Lecture, Course, HomeWork, HomeTask, WorkRate, RateComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'user_type')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, request):
        user = User.objects.create(
            username=request['username'],
            email=request['email'],
            first_name=request['first_name'],
            last_name=request['last_name'],
            user_type=request['user_type']
        )

        user.set_password(request['password'])
        user.save()

        return user


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'users', 'name', 'lectures')
        read_only_fields = ('id', 'lectures')


class LectureSerializer(serializers.ModelSerializer):
    # course = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Lecture
        fields = ('id', 'course', 'topic', 'presentation', 'hometasks')


class HomeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTask
        fields = ('id', 'lecture', 'text', 'homeworks')


class HomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = ('id', 'task', 'student', 'work')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkRate
        fields = ('id', 'work', 'rate', 'comments')




