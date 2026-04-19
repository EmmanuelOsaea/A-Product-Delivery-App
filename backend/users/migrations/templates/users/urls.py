from django.urls  import path
from . import views

app_name = 'orders'

urlpattern = [
    path('', views.OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', views.OrderListView.as_view(), name='order-detail')    
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
]
