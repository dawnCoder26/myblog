from django.conf.urls import url
from . import views

urlpatterns = [
  url('^$',views.index,name='index'),
  url('about/',views.about,name='about'),
  url('contact/',views.contact,name='contact'),
  url('details/(?P<id>\d+)/$',views.details,name='details')
];
