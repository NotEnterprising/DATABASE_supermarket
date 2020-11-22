from django.urls import path

from .views import SupplierListView, SupplierCreateView, SupplierUpdateView, SupplierDetailView, SupplierDeleteView

urlpatterns = [
  path('list/', SupplierListView.as_view(), name='supplier-list'),
  path('<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
  path('create/', SupplierCreateView.as_view(), name='supplier-create'),
  path('<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier-update'),
  path('<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier-delete'),
]
