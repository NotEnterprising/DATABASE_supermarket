from django.urls import path

from .views import CommodityListView, CommodityCreateView, CommodityUpdateView, CommodityDetailView, CommodityDeleteView

urlpatterns = [
  path('list/', CommodityListView.as_view(), name='commodity-list'),
  path('<int:pk>/', CommodityDetailView.as_view(), name='commodity-detail'),
  path('create/', CommodityCreateView.as_view(), name='commodity-create'),
  path('<int:pk>/update/', CommodityUpdateView.as_view(), name='commodity-update'),
  path('<int:pk>/delete/', CommodityDeleteView.as_view(), name='commodity-delete'),
]
