from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sh_questions.views.home'),
    url(r'(?P<request_query>.+)$', 'sh_questions.views.home'),

)
