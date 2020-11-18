from django.urls import path

from .views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDetailView, CustomerDeleteView

urlpatterns = [
  path('list/', CustomerListView.as_view(), name='Customer-list'),
  path('<int:pk>/', CustomerDetailView.as_view(), name='Customer-detail'),
  path('create/', CustomerCreateView.as_view(), name='Customer-create'),
  path('<int:pk>/update/', CustomerUpdateView.as_view(), name='Customer-update'),
  path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='Customer-delete'),
]
