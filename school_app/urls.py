"""newapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
                  # path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', include('account.urls')),
                  path('', include('corecode.urls')),
                  path('staff/', include('staff.urls')),
                  path('admin/', include('admin.urls')),
                  path('customer/', include('customer.urls')),
                  path('supermarket/', include('supermarket.urls')),
                  path('supermarketToActivity/', include('supermarketToactivity.urls')),
                  path('supermarketToExpress/', include('supermarketToexpress.urls')),
                  path('purchase/', include('purchase.urls')),
                  path('express/', include('express.urls')),
                  path('activity/', include('activity.urls')),
                  path('department/', include('department.urls')),
                  path('category/', include('category.urls')),
                  path('commodity/', include('commodity.urls')),
                  path('warehouse/', include('warehouse.urls')),
                  path('supplier/', include('supplier.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
