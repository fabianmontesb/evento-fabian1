"""
URL configuration for academia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('eventos/', views.EventoListView.as_view(), name='lista_eventos'),
    path('eventos/nuevo/', views.EventoCreateView.as_view(), name='nuevo_evento'),
    path('eventos/<int:pk>/', views.EventoDetailView.as_view(), name='detalle_evento'),
    path('inscripcion/<int:evento_id>/', views.inscribir_evento, name='inscribir_evento'),
]
