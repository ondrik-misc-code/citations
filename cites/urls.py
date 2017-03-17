from django.conf.urls import url
from . import views

app_name = 'cites'
urlpatterns = [
    # ex: /cites/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /cites/pub/5/
    url(r'^pub/(?P<pk>[0-9]+)/$', views.pub_detail, name='pub_detail'),
    # url(r'^pub/(?P<pk>[0-9]+)/$', views.PubDetailView.as_view(), name='pub_detail'),
    # ex: /cites/add_pub
    url(r'^add_pub/$', views.add_pub, name='add_pub'),
]
