"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# urls.py
from django.contrib import admin
from django.urls import path
from secondapp import views as v1
from . import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/', v1.page),
    path('page1/', v1.page1),
    path('page2/', v1.page2),
    path('img_2/', v1.img_07),
    path('dete/', v1.detect_objects),
    path('dete2/', v1.detect2_objects),
    path('dete3/', v1.detect3_objects),
    path('dete4/', v1.detect4_objects),
    path('map_p/', v1.map_page),
    # Other URL patterns...

]


