"""
URL configuration for agenda_planify_django project.

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
from django.urls import path
from agenda_planify.views.view_activity import ActivityList, ActivityDetail
from agenda_planify.views.view_pt_ftl import Pt_FTLDetail, Pt_FTLList


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='index'),
    
    path('activity/', ActivityList.as_view(), name='item-list'),  # Lista de ítems
    path('activity/<int:pk>/', ActivityDetail.as_view(), name='item-detail'),

    path('pt_ftl/', Pt_FTLList.as_view(), name='item-list'),  # Lista de ítems
    path('pt_ftl/<int:pk>/', Pt_FTLDetail.as_view(), name='item-detail'),

    
]
