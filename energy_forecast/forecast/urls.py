from django.urls import path
from .views import ForecastView

urlpatterns = [
    path('', ForecastView.as_view(), name='forecast'),
    path('forecast/', ForecastView.as_view(), name='forecast'),
]
