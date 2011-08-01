from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", "cij.views.home", name="home"),
    url(r"^registered/$", "cij.views.registered", name="registered"),
    url(r"^club/$", "cij.views.club", name="club"),
    url(r"^pampers/$", "cij.views.pampers", name="pampers"),
    url(r"^contact/$", "cij.views.contact", name="contact"),
    url(r"^confirmation/(?P<num>\d+)*$", "cij.views.confirmation", name="confirmation"),
    url(r"^correction/(?P<num>\d+)*$", "cij.views.correction", name="correction"),
)
