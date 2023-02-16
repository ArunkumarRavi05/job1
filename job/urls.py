"""job URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('candidates.urls')),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('signup/',views.signup, name = "signup"),
    path('signin/',views.signin, name = "signin"),

    path('account/', views.account, name='account'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('', include('candidates.urls')),
    #path('hiring/', include('recruiters.urls')),
    path('', include('pwa.urls')),
    
] + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
