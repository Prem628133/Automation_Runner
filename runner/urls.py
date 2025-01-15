from django.urls import path
from .views import CheckAPI

urlpatterns = [
    path('run-test/', CheckAPI.as_view(), name='run_test'),
]
