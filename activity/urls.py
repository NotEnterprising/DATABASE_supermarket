from django.urls import path

from .views import ActivityListView, ActivityCreateView, ActivityUpdateView, ActivityDetailView, \
    ActivityDeleteView

urlpatterns = [
    path('list/', ActivityListView.as_view(), name='activity-list'),
    path('<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('create/', ActivityCreateView.as_view(), name='activity-create'),
    path('<int:pk>/update/', ActivityUpdateView.as_view(), name='activity-update'),
    path('<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),
]
