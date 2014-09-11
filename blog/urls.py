from django.conf.urls import patterns, include, url
from blog.views import blog

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'astro.views.home', name='home'),
    url(r'^$', blog),

)
