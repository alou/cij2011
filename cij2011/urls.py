from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cij2011.views.home', name='home'),
    # url(r'^cij2011/', include('cij2011.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", "cij.views.home", name="home"),
    url(r"^registered/$", "cij.views.registered", name="registered"),
    url(r"^club/$", "cij.views.club", name="club"),
    url(r"^contact/$", "cij.views.contact", name="contact"),
    url(r"^confirmation/(?P<num>\d+)*$", "cij.views.confirmation", name="confirmation"),
)
