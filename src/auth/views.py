from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') or None
        password = request.POST.get('password') or None
        # eval("print('this is login view')")
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('Login Here!')
                return redirect('/')
    return render(request, 'auth/login.html', {})

def register_view(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username') or None
        email = request.POST.get('email') or None
        password = request.POST.get('password') or None
        #Django forms
        # username_exists = User.objects.filter(username__iexact=username)
        # email_exists = User.objects.filter(email__iexact=email)
        User.objects.create_user(username=username, email=email, password=password)

    return render(request, 'auth/register.html', {})

