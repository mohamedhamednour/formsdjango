"""admin URL Configuration

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
from demo import views
from django.conf.urls import url

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path ('demo',include('demo.urls')),
    path('ad/', views.file , name='bac'),
    path('idd/<int:st_id>/', views.iD , name='lin'),
    path('del/<int:st_i>/', views.delate , name='delate'),
    path('form', views.form, name='form'),
    path('login', views.login, name='login'),
    path('form2', views.addnew , name='form2'),
    path('lo', views.loginbase, name='sign'),
    path('logut', views.logOut , name='logout'),
    path('hi/',views.vi),
    path('APi', views.Apostudent.as_view() , name='APIS')

]
