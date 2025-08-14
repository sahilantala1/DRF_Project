from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('emp',views.EmployeeViewset, basename='employee')

urlpatterns = [
    # path('students/',views.j_data),
    # path('students/<str:id>',views.StudentDetailView),
    # path('emp/',views.Employee.as_view()),
    # path('emp/<int:id>/',views.EmployeeDetails.as_view()),
    # path('',include(router.urls)),
    # path('blogs/',views.BlogView.as_view()),
    # path('comments/',views.CommentView.as_view()),
    # path('blogDetails/<int:id>',views.BlogDetailsView.as_view()),
    # path('commentDetails/<int:id>',views.CommentDetailsView.as_view()),
    path('emp_view/',views.EmployeeViewDetails.as_view())
]