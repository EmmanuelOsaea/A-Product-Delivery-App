from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path = ('admin/', admin.site.urls),
  path = ('delivery/', include ('delivery.urls')),
  path = ('users/', include ('users.urls')),
]

urlpatterns = [
  path = ('orders/', views.OrderListView.as_view(), name='order-list'),
  path = ('orders/'/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail')
  path = ('track/<str:tracking_code>/', views.TrackOrderView.as_view(), name='track-order'),
]

