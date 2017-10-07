from django.conf.urls import url

from home.views import home, about

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^about/$', about, name="about"),
]