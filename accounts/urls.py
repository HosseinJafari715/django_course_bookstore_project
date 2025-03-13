from django.urls import path
from . import views

urlpatterns = [
    path('singnup/', views.SignUpView.as_view(), name='signup'),
]