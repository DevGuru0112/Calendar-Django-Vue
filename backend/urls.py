from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('users/', views.user_list),
    path('api/get_infos', views.get_infos),
    path('api/month/get-info', views.get_month_info),
    path('api/add_resource', views.add_resource),
]
