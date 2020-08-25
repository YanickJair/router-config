from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/admin')), # Make it go to the Admin page
    url(r'^',  include('demo.urls'))
]
