from .views import MainView, ApiView
from django.urls import path

urlpatterns = [
    path('', MainView),
    path('api/', ApiView)
]
