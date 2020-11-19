from django.urls import path

from .views import SupermarketListView, SupermarketCreateView, SupermarketUpdateView, SupermarketDetailView, \
    SupermarketDeleteView

urlpatterns = [
    path('list/', SupermarketListView.as_view(), name='supermarket-list'),
    path('<int:pk>/', SupermarketDetailView.as_view(), name='supermarket-detail'),
    path('create/', SupermarketCreateView.as_view(), name='supermarket-create'),
    path('<int:pk>/update/', SupermarketUpdateView.as_view(), name='supermarket-update'),
    path('<int:pk>/delete/', SupermarketDeleteView.as_view(), name='supermarket-delete'),
]
