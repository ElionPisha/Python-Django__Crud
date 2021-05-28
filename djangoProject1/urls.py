"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from app.views import index, add_book, delete_book, edit_book, UserAccess

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('user.html', UserAccess, name='UserAccess'),
    path('add-book/', add_book, name='add_book'),
    path('delete-book/<int:book>/', delete_book, name='delete_book'),
    path('edit-book/<int:book>/', edit_book, name='edit_book')
]
