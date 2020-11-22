from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.DepartmentListView.as_view(), name='department-list'),
    path('create/', views.DepartmentCreateView.as_view(), name='department-create'),
    path('<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department-update'),
    path('<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department-delete'),
]
