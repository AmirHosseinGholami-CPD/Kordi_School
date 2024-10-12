from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from Staff.models import Staff
from django.contrib.auth.models import User
from Teacher.models import Seven_Teacher_One, Seven_Teacher_Two, Eight_Teacher_One
from Teacher.models import Eight_Teacher_Two, Nine_Teacher_One, Nine_Teacher_Two
from Admin.models import Admin_Web
from Student.models import Seven_Student_One, Seven_Student_Two, Eight_Student_One
from Student.models import Eight_Student_Two, Nine_Student_One, Nine_Student_Two
from .mixins import AdminRequiredMixin
from django.urls import reverse

# View for handling user login
class LoginView(View):
    # Handle GET request
    def get(self, request):
        # Render the login page
        return render(request, 'registration/login.html')

    # Handle POST request
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            teacher_models = [
                Seven_Teacher_One, Seven_Teacher_Two, 
                Eight_Teacher_One, Eight_Teacher_Two, 
                Nine_Teacher_One, Nine_Teacher_Two
            ]

            student_models = [
                Seven_Student_One, Seven_Student_Two, 
                Eight_Student_One, Eight_Student_Two, 
                Nine_Student_One, Nine_Student_Two
            ]

            staff_models = [
                Staff
            ]

            for model in teacher_models:
                try:
                    user = model.objects.get(username=username, password=password)
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('teacher')
                    else:
                        new_user = User.objects.create_user(username=username, password=password)
                        login(request, new_user)
                        return redirect('teacher')
                except model.DoesNotExist:
                    continue

            for model in student_models:
                try:
                    user = model.objects.get(username=username, password=password)
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('student')
                    else:
                        new_user = User.objects.create_user(username=username, password=password)
                        login(request, new_user)
                        return redirect('student')
                except model.DoesNotExist:
                    continue

            for model in staff_models:
                try:
                    user = model.objects.get(username=username, password=password)
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect('management')
                    else:
                        new_user = User.objects.create_user(username=username, password=password)
                        login(request, new_user)
                        return redirect('management')
                except model.DoesNotExist:
                    continue

            try:
                admin_user = Admin_Web.objects.get(username=username, password=password)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('admin')
                else:
                    new_admin_user = User.objects.create_user(username=username, password=password)
                    login(request, new_admin_user)
                    return redirect('admin')
            except Admin_Web.DoesNotExist:
                messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
        else:
            messages.error(request, 'لطفاً همه فیلدها را پر کنید.')
        
        return render(request, 'registration/login.html')

