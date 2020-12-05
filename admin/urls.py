from django.urls import path

from . import views
from .views import AdminListView, AdminUpdateView, AdminDetailView, AdminDeleteView

urlpatterns = [
    path('list/', AdminListView.as_view(), name='admin-list'),
    path('<int:pk>/', AdminDetailView.as_view(), name='admin-detail'),
    path('create/', views.register, name='admin-create'),
    path('<int:pk>/update/', AdminUpdateView.as_view(), name='admin-update'),
    path('<int:pk>/delete/', AdminDeleteView.as_view(), name='admin-delete'),
]
