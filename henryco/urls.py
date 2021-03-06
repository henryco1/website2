"""henryco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import home.views
import contact.views
import projects.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.views.homepage, name='homepage'),
    url(r'^contact/', contact.views.contact, name='contact'),
    # url(r'^contact/success', contact.views.success, name='success'),
    url(r'^projects/', projects.views.projects, name='projects'),
    url(r'^images/', projects.views.projects, name='projects'),
]
