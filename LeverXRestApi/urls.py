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
from rest_framework import routers
from API import views


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)


api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
    # path('', include(router.urls)),
    path('users/', views.UserList.as_view()),
    path('registration/', views.UserRegistration.as_view()),
    path('courses/create', views.CourseCreate.as_view()),
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:course_id>', views.CourseRUD.as_view()),
    path('courses/<int:course_id>/lectures/', views.LectureCreate.as_view()),
    path('courses/<int:course_id>/lectures/<int:lecture_id>/hometasks/', views.HomeTaskCreate.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
