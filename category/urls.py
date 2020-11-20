from django.urls import path

from . import views

urlpatterns = [
    path('category/list/', views.CategoryListView.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
]
