"""
URL configuration for seminario_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from inscripciones import views


app_name = 'inscripciones'

urlpatterns = [
    path('', views.inscripciones_list, name='inscripciones_list'),
    path('agregar/', views.inscripcion_agregar, name='inscripcion_agregar'),
    path('editar/<int:inscripcion_id>/', views.inscripcion_editar, name='inscripcion_editar'),
    path('eliminar/<int:inscripcion_id>/', views.inscripcion_eliminar, name='inscripcion_eliminar'),
]


