"""eTicket URL Configuration

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
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from ticketApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.index, name = 'index'),
    path('organizationDetails/', views.organizationDetails, name = 'organizationDetails'),
    path('billingAddress/', views.billingAddress, name = 'billingAddress'),
    path('paymentMethods/', views.paymentMethods, name = 'paymentMethods'),
    path('changePassword/', views.changePassword, name = 'changePassword'),
    path('ticketGenerator/', include('ticketGenerator.urls')),

    

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

