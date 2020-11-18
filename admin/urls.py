from django.urls import path

from .views import AdminListView, AdminCreateView, AdminUpdateView, AdminDetailView,AdminDeleteView

urlpatterns = [
  path('list/', AdminListView.as_view(), name='admin-list'),
  path('<int:pk>/', AdminDetailView.as_view(), name='admin-detail'),
  path('create/', AdminCreateView.as_view(), name='admin-create'),
  path('<int:pk>/update/', AdminUpdateView.as_view(), name='admin-update'),
  path('<int:pk>/delete/', AdminDeleteView.as_view(), name='admin-delete'),
]
