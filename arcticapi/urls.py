"""arcticapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings

from api.views import indexView, resultsView, loginView, addView, addresultsView, nbahomeView, agentindexView, agentresultsView, coach2indexView, coach2resultsView # import view here  routes start with the app not project name
from django.conf.urls import url


urlpatterns = [
    url(r'nbahome/', nbahomeView, name='nbahomeView'), # connects map with view function
    url(r'agentprediction/', agentindexView, name='agentindexView'), # connects map with view function
    url(r'agentresults/', agentresultsView, name='agentresultsView'),
    url(r'coach2prediction/', coach2indexView, name='coach2indexView'), # connects map with view function
    url(r'coach2results/', coach2resultsView, name='coach2resultsView'),
    url(r'add/', addView, name='addView'), # connects map with view function
    url(r'addresults/', addresultsView, name='addresultsView'), # connects map with view function
    url(r'prediction/', indexView, name='indexView'), # connects map with view function
    url(r'results/', resultsView, name='resultsView'),
    url(r'login/', loginView, name='loginView'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(r'^.*/',include('client.urls')),
    re_path('', include('client.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
