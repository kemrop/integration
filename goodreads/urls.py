__author__ = 'markrop'
from django.conf.urls import patterns, url
from goodreads import views
urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)