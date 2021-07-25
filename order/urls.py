from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('buy/<int:pk>', views.Buy.as_view(), name='buy'),
    path('saveorder/', views.SaveOrder.as_view(), name='saveorder'),
    path('list/', views.List.as_view(), name='list'),
    path('details/<int:pk>', views.Details.as_view(), name='details'),
]
