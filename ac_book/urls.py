from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.consume_list, name='consume_list'),
]