"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.views.generic.base import RedirectView, TemplateView
from uploadapp.views import *

# from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('uploadapp.urls')),
    path('', include('uploadapp.urls')),
    # url(r'^.*', TemplateView.as_view(template_name="index.html"), name="index")
    #path('', RedirectView.as_view(url='index.html'), name='home'),
    # url(r'^$', RedirectView.as_view(url='/static/index.html'), name='home')
    url(r'^$', RedirectView.as_view(url='https://keends-frontend.herokuapp.com/'), name='home')
    #url(r'^$', serve,kwargs={'path': 'index.html'}),  
    # 
    # kinda works....html unexpected < in index.html  
    #url(r'^(?P<path>.*)/$', index)

    # url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        # RedirectView.as_view(url='/static/%(path)s', permanent=False)),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
