from django.views.generic import ListView, DetailView, CreatView
from .models import Order
from .forms import OrderFrom

class OrderListView(ListView):
   model = Order
   template_name = 'orders/order_list.html
   context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = order
    template_name = 'orders/order_detail.html'
    

class OrderCreateView(CreateView):
     model = Order
     form_class = OrderForm
     template_form = 'orders/order_form.html'
     success_url = '/orders/'
  

