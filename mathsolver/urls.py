from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mathsolver'

urlpatterns = [
    path("home", views.math_problem_solver, name = "home")
]

