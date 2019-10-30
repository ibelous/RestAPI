"""LeverXRestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from API import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Classroom API')


comments_patterns = [
    path('comments/create/', views.CommentCreate.as_view()),
    path('comments/', views.CommentList.as_view()),
]

rate_patterns = [
    path('rate/create/', views.HomeWorkRateCreate.as_view()),
    path('rate/', views.HomeWorkRateR.as_view()),
    path('rate/', include(comments_patterns)),
]

homeworks_patterns = [
    path('homeworks/create/', views.HomeWorkCreate.as_view()),
    path('homeworks/', views.HomeWorkList.as_view()),
    path('homeworks/all/', views.AllHomeWorkList.as_view()),
    path('homeworks/<int:homework_id>/', views.HomeWorkRU.as_view()),
    path('homeworks/<int:homework_id>/', include(rate_patterns)),
]

hometasks_patterns = [
    path('hometasks/create/', views.HomeTaskCreate.as_view()),
    path('hometasks/', views.HomeTaskList.as_view()),
    path('hometasks/<pk>/', views.HomeTaskList.as_view()),
    path('hometasks/<int:hometask_id>/', include(homeworks_patterns)),
]

lectures_patterns = [
    path('lectures/create/', views.LectureCreate.as_view()),
    path('lectures/', views.LectureList.as_view()),
    path('lectures/<pk>/', views.LectureRUD.as_view()),
    path('lectures/<int:lecture_id>/', include(hometasks_patterns)),
]

urlpatterns = [
    url(r'^$', schema_view),
    path('admin/', admin.site.urls),
    path('users/', views.UserList.as_view()),
    path('registration/', views.UserRegistration.as_view()),
    path('courses/create/', views.CourseCreate.as_view()),
    path('courses/', views.CourseList.as_view()),
    path('courses/<pk>/', views.CourseRUD.as_view()),
    path('courses/<int:course_id>/', include(lectures_patterns)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
