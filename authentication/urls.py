from django.urls import path
from .views import Shop
urlpatterns=[
    path('shop/', Shop.as_view())
]