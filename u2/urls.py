from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'u2_app.views.index'), # root
    url(r'^login$', 'u2_app.views.login_view'), # login
    url(r'^logout$', 'u2_app.views.logout_view'), # logout
    url(r'^signup$', 'u2_app.views.signup'), # signup
)