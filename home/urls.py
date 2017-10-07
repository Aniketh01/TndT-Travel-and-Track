from django.conf.urls import url

from home.views import home, about, contact

urlpatterns = [
    url(r'^$', home, name="home"),
]