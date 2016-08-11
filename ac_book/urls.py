from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.consume_list, name='consume_list'),
	url(r'^consume/(?P<pk>[0-9]+)$', views.consume_detail, name='consume_detail'),
	url(r'^consume/new/$', views.consume_new, name='consume_new'),
	url(r'^consume/(?P<pk>[0-9]+)/edit/$', views.consume_edit, name = 'consume_edit'),
]