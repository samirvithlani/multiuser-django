from django.contrib import admin
from django.urls import path,include

from .views import TeacherSignupView

urlpatterns = [

    path("teachersignup/",TeacherSignupView.as_view(),name="teachersignup"),
]
