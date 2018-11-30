from django.shortcuts import render


def sigmus_2018_wajima(request):
  return render(request, 'interface/documents/sigmus_2018_wajima.html')


def master_experiment(request):
  return render(request, 'interface/documents/master_experiment.html')
