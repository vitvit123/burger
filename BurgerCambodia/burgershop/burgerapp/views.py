from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import login

def homepage(request):
    template = 'home.html'
    return render(request, template)

def menu(request):
    template = 'menu.html'
    return render(request, template)

def promotion(request):
    template = 'promotion.html'
    return render(request, template)

def aboutus(request):
    template = 'about.html'
    return render(request, template)

def contactus(request):
    template = 'contactus.html'
    return render(request, template)

def news(request):
    template = 'news.html'
    return render(request, template)

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        sex = request.POST.get('sex')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_image = request.FILES.get('profile_image')

        # Create a new User object
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create a new UserProfile object
        user_profile = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            sex=sex,
            dob=dob,
            profile_image=profile_image
        )

        # Login the user
        login(request, user)

        # Redirect to a success page or the user's profile page
        return redirect('homepage')

    template = 'signup.html'
    return render(request, template)