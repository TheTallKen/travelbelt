from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success), #---> Turn this to /travels :O
    url(r'^login$', views.login),
    url(r'^add$', views.add),
    url(r'^addtravel$', views.addtravel),
    url(r'^travel/(?P<id>\d+)$', views.travel, name='travel'),
    #url(r'^travels$', views.travels),
]