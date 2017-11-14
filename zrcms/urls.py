"""zrcms URL Configuration

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
from django.contrib.auth import views as auth_views

from zrcms.utils.healthutil import health_check
from zruser.views import login_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_view, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^user/', include('zruser.urls', namespace='user')),
    url(r'^transactions/', include('zrtransaction.urls', namespace='transaction')),
    url(r'^payment_request/', include('zrpayment.urls', namespace='payment-requests')),
    url(r'^commission/', include('zrcommission.urls', namespace='commission')),
    url(r'^wallet/', include('zrwallet.urls', namespace='wallet')),
    url(r'^health_check/', health_check),
]
