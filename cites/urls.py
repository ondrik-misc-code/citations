from django.conf.urls import url
from . import views

app_name = 'cites'
urlpatterns = [
    # ex: /cites/
    url(r'^$', views.index, name='index'),
    # ex: /cites/pub/5/
    url(r'^(?P<pub_id>[0-9]+)/$', views.pub_detail, name='pub_detail'),
]
