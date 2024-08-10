from django.shortcuts import render, redirect
from app.models import Attendance, Employees
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "index.html")


def attendance_create(request, id):
    if request.method == "POST":
        employee = Employees.objects.filter(id=id)
        # attendance = Attendance()
        # attendance.employee = employee
        # attendance.save()
        Attendance.objects.create(employee=employee)
        return redirect("staff_list")
    else:
        return render(request, "create.html")


def staff_list(request):
    attendances = Attendance.objects.all()
    context = {"attendances": attendances}
    return render(request, "list.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            print("1111111111")
            login(request, user)
            return redirect("index")
        return render(request, "login.html")

    return render(request, "login.html")


@login_required
def update(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":

        user.username = request.POST["username"]
        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.save()

        return redirect("index")
    else:
        return render(request, "update.html", {"user": user})


@login_required
def employee_creat(request):
    if request.method == "POST":
        Employees.objects.create(
            full_name=request.POST["full_name"],
            phone=request.POST["phone"],
            email=request.POST["email"],
        )
        return redirect("index")
    return render(request, "employee-create.html")


@login_required
def employee_update(request, id):
    employee = Employees.objects.get(id=id)
    if request.method == "POST":
        employee.full_name = request.POST["full_name"]
        employee.phone = request.POST["phone"]
        employee.email = request.POST["email"]
        employee.save()
        return redirect("index")
    return render(request, "employee-update.html", {"employee": employee})


@login_required
def employee_delete(request, id):
    Employees.objects.get(id=id).delete()
    return redirect("index")
