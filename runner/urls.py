from django.urls import path
from .views import CheckApiView

urlpatterns = [
    path('run-test/', CheckApiView.as_view(), name='run_test'),
]
