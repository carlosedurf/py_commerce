from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.Buy.as_view(), name='buy'),
    path('saveorder/', views.SaveOrder.as_view(), name='saveorder'),
    path('details/', views.Details.as_view(), name='details'),
]
