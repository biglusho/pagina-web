from django.urls import path
from .views import home
from .views import contacto
from .views import terminos_condiciones
from .views import registro

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('terminosytondiciones/', terminos_condiciones, name="terminosYcondiciones"),
    path('registro/', registro, name="registro"),
]