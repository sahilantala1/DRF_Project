from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.j_data),
    path('students/<str:id>',views.StudentDetailView),
    path('emp/',views.Employee.as_view()),
    path('emp/<int:id>/',views.Employee_update.as_view())
]