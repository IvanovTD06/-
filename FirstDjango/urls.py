"""
URL configuration for FirstDjango project.

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
from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    # Путь к главной странице
    path('', views.main_page),

    # Пути первичных функций

    path("Teacher register.html", views.teacher_registration),
    path("TR submit", views.get_TRF_form),
    path("Discipline register.html", views.discipline_registration),
    path("DR submit", views.get_DRF_form),
    path("Equipment register.html", views.equipment_registration),
    path("ER submit", views.get_ERF_form),
    path("Building register.html", views.building_registration),
    path("BR submit", views.get_BRF_form),
    path("Cabinet type register.html", views.cabinet_type_registration),
    path("CTR submit", views.get_CTRF_form),
    
    # Пути вторичных функций

    path("Cabinet register.html", views.cabinet_registration),
    path("CR submit", views.get_CRF_form),

    #Создание/удаление/настройки базы данных
    path("create_db", views.db_create_button),
    path("drop_db", views.db_drop_button),
    path("registrate connection", views.registrate_connection)
]
