from django.views.generic import ListView, DetailView, CreateView
from .models import Order
from .forms import OrderFrom
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .payment import PaymentProcessor

class OrderListView(ListView):
   model = Order
   template_name = 'orders/order_list.html'
   context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = order
    template_name = 'orders/order_detail.html'
    

class OrderCreateView(CreateView):
     model = Order
     form_class = OrderForm
     template_name = 'orders/order_form.html'
     success_url = '/orders/'

class CreatePaymentIntentView(APIView):
    def post(self, request):
       amount = request.data.get('amount')
       if not amount:
           return Response({'error': 'Amount is required'), status=status.HTTP_400_BAD_REQUEST)

      try:
         amount_cents = int(float(amount) * 100) Converts dollars to cents
         client_secret = PaymentProcess.create_process_intent(amount_cents)
         return Response({'client_secret': client_secret})
     except Exception as e:
         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
              
  

