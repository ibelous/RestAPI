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
        fields = ('id', 'topic', 'presentation', 'course', 'hometasks')
        read_only_fields = ('course', 'hometasks')

    def create(self, validated_data):
        course_id = self.context['view'].kwargs['course_id']
        course = Course.objects.get(id=course_id)
        lecture = Lecture.objects.create(course=course,
                                         topic=validated_data['topic'],
                                         presentation=validated_data['presentation'])
        lecture.save()
        return lecture


class LectureRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'topic', 'presentation', 'hometasks')


class HomeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTask
        fields = ('id', 'lecture', 'text', 'homeworks')
        read_only_fields = ('lecture', 'homeworks')

    def create(self, validated_data):
        lecture_id = self.context['view'].kwargs['lecture_id']
        lecture = Lecture.objects.get(id=lecture_id)
        hometask = HomeTask.objects.create(lecture=lecture,
                                           text=validated_data['text'], )
        hometask.save()
        return hometask


class HomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = ('id', 'task', 'student', 'work', 'rate')
        read_only_fields = ('student', 'task', 'rate')

    def create(self, validated_data):
        hometask_id = self.context['view'].kwargs['hometask_id']
        hometask = HomeTask.objects.get(id=hometask_id)
        user = self.context['view'].request.user
        homework = HomeWork.objects.create(task=hometask,
                                           student=user,
                                           work=validated_data['work'], )
        homework.save()
        return homework


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkRate
        fields = ('id', 'work', 'rate', 'comments')
        read_only_fields = ('work', 'comments')

    def create(self, validated_data):
        homework_id = self.context['view'].kwargs['homework_id']
        homework = HomeWork.objects.get(id=homework_id)
        workrate = WorkRate.objects.create(work=homework,
                                           rate=validated_data['rate'], )
        workrate.save()
        return workrate


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateComment
        fields = ('id', 'rate', 'author', 'comment')
        read_only_fields = ('rate', 'author')

    def create(self, validated_data):
        homework_id = self.context['view'].kwargs['homework_id']
        homework = HomeWork.objects.get(id=homework_id)
        workrate = WorkRate.objects.get(work=homework)
        author = self.context['view'].request.user
        comment = RateComment.objects.create(rate=workrate,
                                             author=author,
                                             comment=validated_data['comment'])
        comment.save()
        return comment
