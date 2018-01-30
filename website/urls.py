from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='Home'),
    url(r'^article/?$', views.ArticleView.as_view(), name='Article'),
    url(r'^user/(?P<username>\w{0,50})/profile/?$', views.ArticleView.as_view(), name='Article'),
]