from django.shortcuts import render, redirect
from .profile import profile

def Root(request):
  return redirect('/home/')

def Home(request):
  return render(request, 'home.html')

def Profile(request):
  content = {
    'profile': profile
  }
  return render(request, 'profile.html', content)
