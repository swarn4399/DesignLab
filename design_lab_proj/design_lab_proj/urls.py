"""design_lab_proj URL Configuration

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

from raisemodifyorder.views import raiseorder
from raisemodifyorder.views import modifyorder
from raisemodifyorder.views import signin
from raisemodifyorder.views import dashboard_foodseeker
from raisemodifyorder.views import header

urlpatterns = [
    path('admin/', admin.site.urls),
    path('raisemodifyorder/raiseorder.html', raiseorder, name='raiseorder'),
    path('raisemodifyorder/modifyorder.html', modifyorder, name='modifyorder'),
    path('raisemodifyorder/signin.html', signin, name='signin'),
    path('raisemodifyorder/dashboard_foodseeker.html', dashboard_foodseeker, name='dashboard_foodseeker'),
    path('raisemodifyorder/header.html',header, name='header')
]
