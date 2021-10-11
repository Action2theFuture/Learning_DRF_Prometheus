from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('django_prometheus.urls')),
    path('user/', include('user.urls'))
]
