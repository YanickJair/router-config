from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^generator', views.generator, name='generator'),
]