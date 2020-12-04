from django.urls import path

from . import views
from .views import categorylist

urlpatterns = [
    path('list/', categorylist, name='category-list'),
    path('create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]
