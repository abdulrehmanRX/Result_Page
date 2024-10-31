from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from .models import StudentResult
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



@login_required
def upload_result(request):
    try:
        if request.method == "POST":
            student_name = request.POST['student_name']
            roll_number = request.POST['roll_number']
            subject = request.POST['subject']
            marks = request.POST['marks']
            StudentResult.objects.create(
                student_name=student_name,
                roll_number=roll_number,
                subject=subject,
                marks=marks
            )
        return render(request, 'upload.html')
    except:
        return render(request, "error.html")





def view_result(request):
    if request.method == "POST":
        roll_number = request.POST['roll_number']
        result = StudentResult.objects.filter(roll_number=roll_number)
        return render(request, 'view.html', {'result': result})
    return render(request, 'search.html')

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_result')  # Redirect after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')



from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')


def home_page(request):
    return render(request, 'index.html')
