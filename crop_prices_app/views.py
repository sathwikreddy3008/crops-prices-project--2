# crop_prices_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from homepage.models import Crop
from .models import Price
from .forms import SignUpForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crop_prices:prices')
        else:
            messages.error(request, 'Invalid login credentials.')
    return render(request, 'login.html')

@login_required(login_url='crop_prices:login')
def logout_view(request):
    logout(request)
    return redirect('crop_prices:login')

@login_required(login_url='crop_prices:login')
def prices(request):
    crops = Crop.objects.all()
    prices = Price.objects.filter(date__lte='2024-01-18')[:10]
    return render(request, 'prices.html', {'crops': crops, 'prices': prices})

def home(request):
    return render(request, 'home.html')

'''def home(request):
    if request.method == 'POST':
        selected_state = request.POST.get('selected_state')
        # Do something with the selected_state, e.g., redirect to prices page
        return redirect('prices')

    crops = Crop.objects.all()
    prices = Price.objects.all()
    context = {
        'crops': crops,
        'prices': prices,
    }
    return render(request, 'home.html', context)'''


def crop_prices_prices(request):
    return render(request, 'prices/prices.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('crop_prices:home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

'''def process_state(request):
    return redirect('')'''