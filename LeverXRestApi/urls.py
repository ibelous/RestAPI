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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Classroom API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
# router.register(r'users', views.UserList)


api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]

comments_patterns = [
    path('comments/', views.HomeWorkRateRU.as_view()),
]

rate_patterns = [
    path('rate/', views.HomeWorkRateRU.as_view()),
    path('rate/', include(comments_patterns)),
]

homeworks_patterns = [
    path('homeworks/create/', views.HomeWorkCreate.as_view()),
    path('homeworks/', views.HomeWorkList.as_view()),
    path('homeworks/<int:homework_id>/', views.HomeWorkRUD.as_view()),
    path('homeworks/<int:homework_id>/', include(rate_patterns)),
]

hometasks_patterns = [
    path('hometasks/create/', views.HomeTaskCreate.as_view()),
    path('hometasks/', views.HomeTaskList.as_view()),
    path('hometasks/<int:hometask_id>/', views.HomeTaskRUD.as_view()),
    path('hometasks/<int:hometask_id>/', include(homeworks_patterns)),
]

lectures_patterns = [
    path('lectures/create/', views.LectureCreate.as_view()),
    path('lectures/', views.LectureList.as_view()),
    path('lectures/<int:lecture_id>/', views.LectureRUD.as_view()),
    path('lectures/<int:lecture_id>/', include(hometasks_patterns)),
]

urlpatterns = [
    path(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
    # path('', include(router.urls)),
    path('users/', views.UserList.as_view()),
    path('registration/', views.UserRegistration.as_view()),
    path('courses/create/', views.CourseCreate.as_view()),
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:course_id>/', views.CourseRUD.as_view()),
    path('courses/<int:course_id>/', include(lectures_patterns)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
