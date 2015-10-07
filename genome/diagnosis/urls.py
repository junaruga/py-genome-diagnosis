from django.conf.urls import url

from diagnosis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<disease_id>[0-9]+)/results/$', views.results, name='results'),
]
