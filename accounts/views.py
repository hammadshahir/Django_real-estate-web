from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contacts


# Create your views here.

def register(request):
    # Logic to check if form is post or get request

    if request.method == 'POST':

        # Get Form Values

        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validation: Password Match

        if password == password2:
            # Check username are duplicate or not
            if User.objects.filter(username=username).exists():
                messages.errorr(request, 'Username is not available. Try an other one!')
                return redirect('register')

            # Check Emails are duplicate or not
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Account with this email already exists!')
                    return redirect('register')
                else:
                # Method 1: Direct login after registeration -- automatically logged in
                    #user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    #auth.login(request, user)
                    #messages.success(request, 'You are successfully logged in')
                    #return redirect('index')
                # Method 2: First register and then log in
                    user.save()
                    messages.success(request, 'You are successfully registered and can log in')
                    return redirect('login')
            return
        else:
            messages.error(request, 'Passwords do not match. Type carefully.')
            return redirect('register')


    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login use Logic
        username = request.POST['username']
        password = request.POST['password']

        # authetication
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid User Name or Password')
            return redirect(request, 'login')
        return
    return render(request, 'accounts/login.html')

def dashboard(request):
    user_contacts = Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
