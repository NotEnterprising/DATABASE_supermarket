from django.urls import path

from .views import WarehouseListView, WarehouseCreateView, WarehouseUpdateView, WarehouseDetailView, WarehouseDeleteView

urlpatterns = [
  path('list/', WarehouseListView.as_view(), name='warehouse-list'),
  path('<int:pk>/', WarehouseDetailView.as_view(), name='warehouse-detail'),
  path('create/', WarehouseCreateView.as_view(), name='warehouse-create'),
  path('<int:pk>/update/', WarehouseUpdateView.as_view(), name='warehouse-update'),
  path('<int:pk>/delete/', WarehouseDeleteView.as_view(), name='warehouse-delete'),
]
