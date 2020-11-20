from django.urls import path

from .views import ActivityListView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView

urlpatterns = [
    path('list/', ActivityListView.as_view(), name='activity-list'),
    path('create/', ActivityCreateView.as_view(), name='activity-create'),
    path('<int:pk>/update/', ActivityUpdateView.as_view(), name='activity-update'),
    path('<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),
]
