"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from APP1.views import *
from APP2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('APP1_first/', APP1_first, name='APP1_first'),
    path('APP2_first/', APP2_first, name='APP2_first'),
    path('APP1_second/', APP1_second, name='APP1_second'),
    path('APP2_second/', APP2_second, name='APP2_second'),
]
