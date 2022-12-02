from django.urls import path

from buy_together_app import views


urlpatterns = [
    path('', views.index, name='supplierPoduct_list')
]
