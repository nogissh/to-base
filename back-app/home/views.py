from django.shortcuts import render, redirect


def Root(request):
  return redirect('/home/')

def Home(request):
  return render(request, 'home.html')

def Profile(request):
  return render(request, 'profile.html')
