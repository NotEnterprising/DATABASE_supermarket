from django.urls import path

from .views import create_purchase, edit_purchase, all_results_view

urlpatterns = [
  path('create-purchase/', create_purchase, name='create-purchase'),
  path('edit-purchase/', edit_purchase, name='edit-purchase'),
  path('view-purchase/', all_results_view, name='view-purchase'),
]
