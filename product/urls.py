from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ListProduct.as_view(), name='list'),
    path('<slug>', views.ProductDetails.as_view(), name='details'),
    path('addtocar/', views.AddCar.as_view(), name='addtocar'),
    path('removetocar/', views.RemoveCar.as_view(), name='removetocar'),
    path('car/', views.Car.as_view(), name='car'),
    path('finally/', views.Finally.as_view(), name='finally'),
]
