from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^andan/', include('andan.urls')),
    url(r'^admin/', admin.site.urls),
]
