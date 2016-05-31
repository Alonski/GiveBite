from django.conf.urls import url
from . import views

app_name = 'bite'
urlpatterns = [
    url(r'^$', views.RestaurantListView.as_view(), name='index'),
    url(r'^restaurant/$', views.RestaurantListView.as_view(), name='restaurant_list'),
    url(r'^restaurant/(?P<pk>[0-9]+)/$', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/dishes/$', views.ListDishes.as_view(), name='dishes_list'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/dishes/add$', views.DishCreateView.as_view(), name='dishes_add'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/dishes/(?P<dish_id>[0-9]+)/$', views.DishViewView.as_view(), name='dishes_view'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/dishes/(?P<dish_id>[0-9]+)/delete/$', views.DishDeleteView.as_view(), name='dishes_delete'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/dishes/(?P<dish_id>[0-9]+)/update/$', views.DishUpdateView.as_view(), name='dishes_update'),
]
