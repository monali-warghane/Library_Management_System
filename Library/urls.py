"""Library_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import home, addbooks, viewbooks, issuebook, returnbook, issuedbook, updatebook, deletebook, registeradmin,loginpage

urlpatterns = [
    path('', home),

    path('addbooks', addbooks.as_view()),
    path('viewbooks', viewbooks.as_view()),
    path('issuebook', issuebook.as_view()),
    path('returnbook', returnbook.as_view()),
    path('issuedbook', issuedbook.as_view()),
    path('updatebook/<str:pk>', updatebook.as_view()),
    path('deletebook/<str:pk>', deletebook.as_view()),
    path('registeradmin', registeradmin),
    path('loginpage', loginpage),
    path('delete/<str:pk>', deletebook.as_view()),
]
