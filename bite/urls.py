from django.conf.urls import url
from . import views

app_name = 'bite'
urlpatterns = [
    url(r'^$', views.RestaurantListView.as_view(), name='index'),
    url(r'^restaurant/$', views.RestaurantListView.as_view(), name='restaurant_list'),
    url(r'^restaurant/add/$', views.RestaurantCreateView.as_view(), name='restaurant_add'),
    url(r'^restaurant/(?P<pk>[0-9]+)/$', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    url(r'^restaurant/(?P<pk>[0-9]+)/delete/$', views.RestaurantDeleteView.as_view(), name='restaurant_delete'),
    url(r'^restaurant/(?P<pk>[0-9]+)/update/$', views.RestaurantUpdateView.as_view(), name='restaurant_update'),
    url(r'^restaurant/(?P<pk>[0-9]+)/order/$', views.OrderView.as_view(), name='user_order'),
    url(r'^restaurant/(?P<pk>[0-9]+)/our-orders/$', views.OrderListView.as_view(), name='restaurant_orders'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/menu/$', views.DishListView.as_view(), name='dishes_list'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/menu/add/$', views.DishCreateView.as_view(), name='dishes_add'),
    # url(r'^restaurant/(?P<restaurant_id>[0-9]+)/menu/(?P<pk>[0-9]+)/$', views.DishViewView.as_view(), name='dishes_view'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/menu/(?P<pk>[0-9]+)/delete/$', views.DishDeleteView.as_view(), name='dishes_delete'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/menu/(?P<pk>[0-9]+)/update/$', views.DishUpdateView.as_view(), name='dishes_update'),
]
