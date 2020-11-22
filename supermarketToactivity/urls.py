from django.urls import path

from .views import create_result, edit_results, all_results_view

urlpatterns = [
  path('create/', create_result, name='create-SupermarketToActivity'),
  path('edit-results/', edit_results, name='edit-SupermarketToActivity'),
  path('view/all', all_results_view, name='view-SupermarketToActivity'),
]
