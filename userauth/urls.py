from django.conf.urls import url

from userauth.views import login, about, contact

urlpatterns = [
    url(r'^$', login, name="login"),

    url(r'^about/', about),
    url(r'^about/', contact),
]
