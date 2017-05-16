"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from vrp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'rankruntimejson1',views.rankruntime1),
    url(r'rankruntimejson2',views.rankruntime2),
    url(r'rankruntimejson3',views.rankruntime3),
    url(r'rankruntimejson4',views.rankruntime4),
    url(r'rankruntimejson5',views.rankruntime5),
    url(r'rankruntimejson6',views.rankruntime6),
    url(r'rankruntimejson7',views.rankruntime7),
    url(r'^rank.html/',views.rank),
    url(r'^$',views.car),
    url(r'linkdatajson', views.linkdata),
    url(r'^link',views.link),
    url(r'geneticjson',views.receivejsongenetic),
    url(r'clusteringjson',views.receivejsonclustering),
    url(r'antjson', views.receivejsonant),
]
