from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.Buy.as_view(), name='buy'),
    path('closeorder/', views.CloseOrder.as_view(), name='closeorder'),
    path('details/', views.Details.as_view(), name='details'),
]
