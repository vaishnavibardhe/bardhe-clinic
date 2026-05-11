from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
import json

# Admin Login View
def admin_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        # Fixed username password
        if username == "Lokeshbardhe" and password == "Lokesh@123":
            
            return redirect('admin_dashboard')

        else:
            return render(request, 'admin_login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'admin_login.html')


@login_required(login_url='/admin_login/')  # Important: Yeh ensure karega ki pehle login ho
def admin_dashboard(request):
    # Yahan aapka dashboard logic
    return render(request, 'admin_dashboard.html')

# Admin Logout
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

# API to get all appointments (for admin)
@staff_member_required
def get_all_appointments(request):
    # This will be handled by JavaScript reading localStorage
    return JsonResponse({'status': 'ok'})

# API to update appointment status
@staff_member_required
def update_appointment_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        appointment_id = data.get('appointment_id')
        status = data.get('status')
        # Status update will be handled by JavaScript
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def doctor(request):
    return render(request, 'doctor.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def book_appointment(request):
    return render(request, 'appointment.html')

def login(request):
    return render(request, 'login.html')

def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')