from django.conf.urls import url
from . import views

app_name = 'bite'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<restaurant>)\/$', views.DishListView.as_view(), name='dishes')
    url(r'^$', views.RestaurantListView.as_view(), name='list'),
    url(r'^restaurant/(?P<pk>[0-9]+)/$', views.RestaurantDetailView.as_view(), name='detail'),
]
