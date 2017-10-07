from django.conf.urls import url

from userauth.views import login

urlpatterns = [
    url(r'^$', login, name="login"),
]
