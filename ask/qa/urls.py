from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.test, name="index"), 
	url(r'^question/(\d+)/$', views.test, name="question"),
	url(r'^login/.*$', views.test, name="login"), 
	url(r'^signup/.*$', views.test, name="signup"), 
	url(r'^ask/.*$', views.test, name="ask"), 
	url(r'^popular/.*$', views.test, name="popular"), 
	url(r'^new/.*$', views.test, name="new"), 
]