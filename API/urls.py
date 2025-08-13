from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('emp',views.EmployeeViewset, basename='employee')

urlpatterns = [
    path('students/',views.j_data),
    path('students/<str:id>',views.StudentDetailView),
    # path('emp/',views.Employee.as_view()),
    # path('emp/<int:id>/',views.EmployeeDetails.as_view())
    path('',include(router.urls))
]