from django.urls import path

from .views import ExpressListView, ExpressCreateView, ExpressUpdateView, ExpressDetailView, \
    ExpressDeleteView

urlpatterns = [
    path('list/', ExpressListView.as_view(), name='express-list'),
    path('<int:pk>/', ExpressDetailView.as_view(), name='express-detail'),
    path('create/', ExpressCreateView.as_view(), name='express-create'),
    path('<int:pk>/update/', ExpressUpdateView.as_view(), name='express-update'),
    path('<int:pk>/delete/', ExpressDeleteView.as_view(), name='express-delete'),
]
