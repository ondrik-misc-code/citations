from django.conf.urls import url
from . import views

app_name = 'cites'
urlpatterns = [
    # e.g.: /cites/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # e.g.: /cites/pub/5/
    url(r'^pub/(?P<pk>[0-9]+)/$', views.pub_detail, name='pub_detail'),
    # url(r'^pub/(?P<pk>[0-9]+)/$', views.PubDetailView.as_view(), name='pub_detail'),
    # e.g.: /cites/add_pub
    url(r'^add_pub/$', views.add_pub, name='add_pub'),
    # e.g.: /cites/pub/4/add_cit
    url(r'^pub/(?P<pk>[0-9]+)/add_cit/$', views.add_cit, name='add_cit'),
    # e.g.: /cites/pub/4/del
    url(r'^pub/(?P<pk>[0-9]+)/del/$', views.del_pub, name='del_pub'),
    # e.g.: /cites/pub/4/add_cit
    url(r'^pub/(?P<pub_pk>[0-9]+)/del_cit/(?P<cit_pk>[0-9]+)/$', views.del_cit, name='del_cit'),
    # e.g.: /cites/manage/
    url(r'^manage/$', views.ManageView.as_view(), name='manage_pubs'),
    # e.g.: /cites/list_year/
    url(r'^cit_list_year/$', views.cit_list_year, name='cit_list_year'),
]
