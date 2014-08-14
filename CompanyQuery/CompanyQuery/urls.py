from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CompanyQuery.views.home', name='home'),
    url(r'^sh_questions/', include('sh_question.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
