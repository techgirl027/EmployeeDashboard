from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("index/", views.index, name="index"),
    path("staff-list/", views.staff_list, name="staff_list"),
    path("attendance-create/<int:id>/", views.attendance_create, name="create"),
    path("update/", views.update, name="update"),
    path("employee_creat/", views.employee_creat, name="employee_creat"),
    path("employee_update/<int:id>/", views.employee_update, name="employee_update"),
    path("employee_delete/<int:id>/", views.employee_delete, name="employee_delete"),
]
