"""
URL configuration for TBC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import views as auth_views
from django.urls import path, include
from ATM.views import atm_locators
from . import views

def not_logged_in(user):
    return not user.is_authenticated

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('', include('ChemiSivrce.urls')),
    path('atmLocations', atm_locators, name='atm_locators'),
    path('register/', views.register, name='register'),
    path('login/', user_passes_test(not_logged_in, login_url='homew', redirect_field_name=None)(
        auth_views.LoginView.as_view(template_name='login.html')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
