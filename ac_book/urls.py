from django.conf.urls import url
from . import views
from django.contrib.auth import views as def_views

urlpatterns = [
	url(r'^$', views.consume_list, name='consume_list'),

	#consume R
	url(r'^consume/(?P<term_id>[0-9]{4}-[0-9]{2})/monthly/$', views.consume_monthly, name='consume_monthly'),

	#consume C U D
	url(r'^consume/read/(?P<pk>\d+)/$', views.consume_read, name='consume_read'),
	url(r'^consume/create/$', views.consume_create, name='consume_create'),
	url(r'^consume/update/(?P<pk>\d+)/$', views.consume_update, name = 'consume_update'),
	url(r'^consume/delete/(?P<pk>\d+)/$', views.consume_delete, name='consume_delete'),

	#member url
	url(r'^registration/sign_up/$', views.sign_up, name='sign_up'),
	url(r'^registration/user_info/$', views.user_info, name='user_info'),
	url(r'^registration/user_del/$', views.user_del, name='user_del'),

    url(r'^accounts/login/$', def_views.login, name='login'),
	url(r'^accounts/logout/$', def_views.logout, name='logout', kwargs={'next_page': '/'}),
]