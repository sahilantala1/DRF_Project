from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.j_data),
    path('students/<str:id>',views.StudentDetailView)
]