from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, get_list_or_404, _get_queryset
from django.utils.encoding import force_text
from django.views.generic import *
from .models import *

# Create your views here.
logger = logging.getLogger(__name__)


class RestaurantMixin:
    fields = (
        'name',
        'address',
        'phone',
        'email',
        'active',
        'owner',
        'description',
    )
    success_url = reverse_lazy('bite:restaurant_list')
    model = Restaurant

    # def get(self, request, pk, *args, **kwargs):
    #     """
    #     Overrides get function then adds a model of type Restaurant to the view whose id = restaurant_id
    #     :param restaurant_id: Gets restaurant_id from url (?P<restaurant_id>[0-9]+)
    #     :return: The regular get return. No need to return our self.restaurant model.
    #     """
    #     self.restaurant = get_object_or_404(Restaurant, id=pk)
    #     self.dishes = get_list_or_404(Dish, restaurant=self.restaurant)
    #     return super().get(request, *args, **kwargs)


class IndexView(RestaurantMixin, ListView):
    template_name = 'bite/index.html'
    fields = (
        'name',
        'address',
        'phone',
        'description',
    )
    page_title = "Home"

    # context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return None


class RestaurantListView(RestaurantMixin, ListView):
    page_title = "My Restaurants"


class RestaurantDetailView(RestaurantMixin, DetailView):
    page_title = ''

    def get(self, request, pk, *args, **kwargs):
        """
        Overrides get function then adds a model of type Restaurant to the view whose id = restaurant_id
        :param restaurant_id: Gets restaurant_id from url (?P<restaurant_id>[0-9]+)
        :return: The regular get return. No need to return our self.restaurant model.
        """
        self.restaurant = get_object_or_404(Restaurant, id=pk)
        self.page_title = "{} Information".format(self.restaurant.name)

        def get_list_or_none(klass, *args, **kwargs):
            queryset = _get_queryset(klass)
            obj_list = list(queryset.filter(*args, **kwargs))
            if obj_list:
                return obj_list
            return []

        self.dishes = get_list_or_none(Dish, restaurant=self.restaurant)
        self.orders = get_list_or_none(Order, restaurant=self.restaurant)
        return super().get(request, *args, **kwargs)


class RestaurantCreateView(RestaurantMixin, CreateView):
    page_title = "Add Restaurant"


class RestaurantUpdateView(RestaurantMixin, UpdateView):
    page_title = "Update Restaurant"
    button_label = "Update"

    # def get_success_url(self):
    #     if 'restaurant_id' in self.kwargs:
    #         restaurant_id = self.kwargs['restaurant_id']
    #     else:
    #         restaurant_id = 'none'
    #     return reverse('bite:dishes_list', kwargs={'restaurant_id': restaurant_id})


class RestaurantDeleteView(RestaurantMixin, DeleteView):
    page_title = "Delete Restaurant"
    button_label = "Delete"

    # def get_success_url(self):
    #     if 'restaurant_id' in self.kwargs:
    #         restaurant_id = self.kwargs['restaurant_id']
    #     else:
    #         restaurant_id = 'none'
    #     return reverse('bite:dishes_list', kwargs={'restaurant_id': restaurant_id})


class DishListView(ListView):
    page_title = "Restaurant Menu"
    page_name = "Menu"
    model = Dish

    def get(self, request, restaurant_id, *args, **kwargs):
        """
        Overrides get function then adds a model of type Restaurant to the view whose id = restaurant_id
        :param restaurant_id: Gets restaurant_id from url (?P<restaurant_id>[0-9]+)
        :return: The regular get return. No need to return our self.restaurant model.
        """
        self.restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(restaurant=self.restaurant)


class DishMixin:
    fields = (
        'name',
        'price',
        'description',
        # 'restaurant',
        # 'id',
    )
    # success_url = reverse_lazy('bite:dishes_list')
    model = Dish

    def get(self, request, restaurant_id, *args, **kwargs):
        self.restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if 'restaurant_id' in self.kwargs:
            restaurant_id = self.kwargs['restaurant_id']
        else:
            restaurant_id = 'none'
        form.instance.restaurant_id = restaurant_id
        return super().form_valid(form)


class DishCreateView(DishMixin, CreateView):
    page_title = "Add Dish"

    def get_success_url(self):
        """
        http://stackoverflow.com/questions/11027996/success-url-in-updateview-based-on-passed-value
        http://stackoverflow.com/questions/30681055/providing-parameters-when-reverse-lazy-ing-a-success-url-redirect
        Changes the success_url in such a way that the restaurant_id is passed as a kwarg for use during creating, updating, deleting.
        :return:
        """
        if 'restaurant_id' in self.kwargs:
            restaurant_id = self.kwargs['restaurant_id']
        else:
            restaurant_id = 'none'
        return reverse('bite:dishes_list', kwargs={'restaurant_id': restaurant_id})


class DishUpdateView(DishMixin, UpdateView):
    page_title = "Update Dish"
    button_label = "Update"

    def get_success_url(self):
        if 'restaurant_id' in self.kwargs:
            restaurant_id = self.kwargs['restaurant_id']
        else:
            restaurant_id = 'none'
        return reverse('bite:dishes_list', kwargs={'restaurant_id': restaurant_id})


class DishDeleteView(DishMixin, DeleteView):
    page_title = "Delete Dish"
    button_label = "Delete"

    def get_success_url(self):
        if 'restaurant_id' in self.kwargs:
            restaurant_id = self.kwargs['restaurant_id']
        else:
            restaurant_id = 'none'
        return reverse('bite:dishes_list', kwargs={'restaurant_id': restaurant_id})


class OrderView(ListView):
    page_title = "Order Page"
    template_name = 'bite/order_page.html'
    model = Dish

    # fields = (
    #     'id',
    #     'price',
    #     'dishes',
    #     # 'restaurant',
    #     # 'id',
    # )
    success_url = reverse_lazy('bite:user_order_thanks')

    def get(self, request, *args, **kwargs):
        self.restaurant = get_object_or_404(Restaurant, id=self.kwargs['pk'])
        return super().get(request, *args, **kwargs)

    # def form_valid(self, form):
    #     if 'restaurant_id' in self.kwargs:
    #         restaurant_id = self.kwargs['restaurant_id']
    #     else:
    #         restaurant_id = 'none'
    #     form.instance.restaurant_id = restaurant_id
    #     return super().form_valid(form)

    def get_queryset(self):
        return super().get_queryset().filter(restaurant=self.restaurant)

    # def get_success_url(self):
    #     """
    #     http://stackoverflow.com/questions/11027996/success-url-in-updateview-based-on-passed-value
    #     http://stackoverflow.com/questions/30681055/providing-parameters-when-reverse-lazy-ing-a-success-url-redirect
    #     Changes the success_url in such a way that the restaurant_id is passed as a kwarg for use during creating, updating, deleting.
    #     :return:
    #     """
    #     if 'restaurant_id' in self.kwargs:
    #         restaurant_id = self.kwargs['restaurant_id']
    #     else:
    #         restaurant_id = 'none'
    #     return reverse('bite:dishes_list', kwargs={'restaurant_id': restaurant_id})


class OrderListView(ListView):
    page_title = "Our Orders"
    model = Order

    # def total(self, test):
    #     total_price = 0
    #     for dish in self.dishes:
    #         total_price += dish.price
    #     return self.dishes
    #     # return self.get_queryset().dishes.aggregate(sum=Sum('price'))['sum']

    def get(self, request, *args, **kwargs):
        self.restaurant = get_object_or_404(Restaurant, id=self.kwargs['pk'])

        # def get_list_or_none(klass, *args, **kwargs):
        #     queryset = _get_queryset(klass)
        #     obj_list = list(queryset.filter(*args, **kwargs))
        #     # logger.error(obj_list)
        #     if obj_list:
        #         return obj_list
        #     return []
        #
        # self.dishes = get_list_or_none(Dish, restaurant=self.restaurant)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(restaurant=self.restaurant)
