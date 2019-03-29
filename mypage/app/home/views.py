from django.shortcuts import render, redirect
from .profile import profile

def Root(request):
  return redirect('/home/')

def Home(request):
  content = {
    'profile': profile
  }
  return render(request, 'home.html', content)
