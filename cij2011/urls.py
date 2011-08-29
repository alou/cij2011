from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", "cij.views.home", name="home"),
    url(r"^login$", "cij.views.login", name="login"),
    url(r"^logout$", "cij.views.logout", name="logout"),
    url(r"^registered/$", "cij.views.registered", name="registered"),
    url(r"^club/$", "cij.views.club", name="club"),
    url(r"^pampers/(?P<num>\d+)*$", "cij.views.pampers", name="pampers"),
    url(r"^details/(?P<id>\d+)$", "cij.views.display",\
                                    name="display"),
    url(r"^contact/$", "cij.views.contact", name="contact"),
    url(r"^confirmation/(?P<num>\d+)*$", "cij.views.confirmation", name="confirmation"),
    url(r"^correction/(?P<num>\d+)*$", "cij.views.correction", name="correction"),
    url(r"^ressources$", "cij.views.ressources", name="ressources"),
    url(r'^liste$', \
        "cij.views.export_excel", name='export_excel'),
)
