from django.urls import path
from . import html as returnHtml

app_name = 'interface'
urlpatterns = [
  path('html/documents/sigmus/2018/wajima/', returnHtml.sigmus_2018_wajima),
]
