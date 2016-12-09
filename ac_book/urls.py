from django.conf.urls import url
from . import views
from django.contrib.auth import views as def_views

urlpatterns = [
	url(r'^$', views.consume_list, name='consume_list'),
	url(r'^consume/list/$', views.consume_list_data, name='consume_list_data'),



	#consume R
	url(r'^consume/(?P<date_from>[0-9]{4}[0-9]{2})-(?P<date_to>[0-9]{4}[0-9]{2})/$', views.consume_term, name='consume_term'),

	#consume C U D
	url(r'^consume/read/(?P<pk>\d+)/$', views.consume_read, name='consume_read'),
	url(r'^consume/create/$', views.consume_create, name='consume_create'),
	url(r'^consume/update/(?P<pk>\d+)/$', views.consume_update, name = 'consume_update'),
	url(r'^consume/delete/(?P<pk>\d+)/$', views.consume_delete, name='consume_delete'),

	url(r'^consume/(?P<date_from>[0-9]{4}[0-9]{2})-(?P<date_to>[0-9]{4}[0-9]{2})/concate/()$', views.consume_term, name='consume_term'),

	#custom consume category R
	url(r'^category/consume/readall/$', views.category_consume_readAll, name='category_consume_readAll'),
	# url(r'^category/consume/read/(?P<pk>\d+)/$', views.category_consume_read, name='category_consume_cread'),
	# url(r'^category/create/$', views.category_create, name='category_create'),
	# url(r'^category/update/(?P<pk>\d+)/$', views.category_update, name = 'category_update'),
	# url(r'^category/delete/(?P<pk>\d+)/$', views.category_delete, name='category_delete'),

	#custom social category R
	# url(r'^category/social/readall/$', views.category_readAll, name='category_readAll'),
	# url(r'^category/social/read/(?P<pk>\d+)/$', views.category_read, name='category_read'),
	# url(r'^category/create/$', views.category_create, name='category_create'),
	# url(r'^category/update/(?P<pk>\d+)/$', views.category_update, name = 'category_update'),
	# url(r'^category/delete/(?P<pk>\d+)/$', views.category_delete, name='category_delete'),

	#member url
	url(r'^registration/sign_up/$', views.sign_up, name='sign_up'),
	url(r'^registration/user_info/$', views.user_info, name='user_info'),
	url(r'^registration/user_del/$', views.user_del, name='user_del'),

    url(r'^accounts/login/$', def_views.login, name='login'),
	url(r'^accounts/logout/$', def_views.logout, name='logout', kwargs={'next_page': '/'}),
]