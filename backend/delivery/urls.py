from django.urls  import path
from . import views

app_name = 'delivery'

urlpatterns = [
  path('orders/', views.OrderListView.as_view(), name='order_list'),
  path('orders/<int:pk>/', views.OrderListView.as_view(), name='order_detail'),
  path('tracks/<str:tracking_code>/', views.TrackeOrderView.as_view(), name='track-order'),
