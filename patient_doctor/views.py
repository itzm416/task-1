from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from blog.forms import AppointmentForm

from patient_doctor.models import Appoinment, Profile
from django.contrib.auth.models import User

from django.contrib import messages

from blog.models import Category
import datetime


def category(request):
    category = Category.objects.all()
    return category

# ------------------------------------------

def home(request):
    return render(request, 'home.html', {'category':category(request)})

def dashboard(request):
    if request.user.is_authenticated:

        return render(request, 'dashboard.html', {'category':category(request)})

    else:
        return redirect('l')

def doctor(request):
    if request.user.is_authenticated:
        doctor = Profile.objects.filter(type='Doctor')
        return render(request, 'doctor.html', {'doctor':doctor,'category':category(request)})
    else:
        return redirect('l')

def appoinment(request, slug):
    if request.user.is_authenticated:
        doctor = User.objects.get(username=slug)

        if request.method == 'POST':

            fm = AppointmentForm(request.POST,request.FILES)
            if fm.is_valid():
                time = fm.cleaned_data['start_time']

                t1 = str(time)
                t2 = str(time)
                t3 = str(time)
                x1 = int(t1[0:2])
                x2 = int(t2[3:5])
                x3 = int(t3[6:8])

                e = datetime.datetime(100, 1, 1, x1, x2, x3)
                end_time = e + datetime.timedelta(minutes=45)

                form = fm.save(commit=False)
                form.username = doctor
                form.end_time = end_time
                form.save()
                details = Appoinment.objects.get(username=doctor)
                return render(request, 'detail.html', {'details':details, 'category':category(request)})
            return render(request, 'appoinment.html', {'form':fm, 'category':category(request)})
        else:
            fm = AppointmentForm()
            return render(request, 'appoinment.html', {'form':fm, 'category':category(request)})
    else:
        return redirect('l')

# --------------------------------------------------

def user_logout(request):
    logout(request)
    return redirect('home')

def user_login(request):
    if not request.user.is_authenticated:

        if request.method=='POST':
            username = request.POST['u_name']
            password = request.POST['password']
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('d')
            else:
                messages.warning(request,'username or password is incorrect !')
                return redirect('l')
        
        else:
            return render(request, 'login.html')
    
    else:
        return redirect('d')
    

def user_signup(request):
    if not request.user.is_authenticated:

        if request.method=='POST':
            user_name = request.POST['u_name']
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            email = request.POST['email']
            line1 = request.POST['line1']
            state = request.POST['state']
            city = request.POST['city']
            pincode = request.POST['pincode']
            type = request.POST['type']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            profile_image = request.FILES.get('files')

            if password1 == password2:
                if User.objects.filter(username=user_name).exists():
                    print('user exist')
                users = User.objects.create_user(username=user_name, first_name=f_name, last_name=l_name, email=email, password=password1)
                users.save()
                profile = Profile(username=users, line1=line1, state=state, pincode=pincode, first_name=f_name, type=type, last_name=l_name, city=city, email=email, profile_image = profile_image)
                profile.save()

            else:
                messages.warning(request,'Password Does Not Match !')
                return redirect('s')

            return redirect('l')
        
        else:
            return render(request, 'signup.html')
    
    else:
        return redirect('d')


