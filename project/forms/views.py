from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        user = request.POST['user_name']
        password = request.POST['pass']
        user = auth.authenticate(username=user, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'INVALID USERNAME AND PASSWORD')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['user_name']
        first = request.POST['first_name']
        last = request.POST['last_name']
        mail = request.POST['mail_id']
        password = request.POST['pass']
        cpass = request.POST['cpass']

        if password == cpass:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'USERNAME alerady exist')
                return redirect('register')

            elif User.objects.filter(email=mail).exists():
                messages.info(request, 'EMAIL alerady exist')
                return redirect('register')

            else:
                user = User.objects.create_user(username=name, first_name=first, last_name=last, email=mail,
                                                password=password)
                user.save();
                return redirect('login')
                print('USER CREATED')
        else:
            messages.info(request, 'PASSWORD NOT MATCHED ')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')