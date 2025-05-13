from django.urls import path
from .views import EnergyBalanceListCreateView
from .views import EnergyBalanceUploadView

urlpatterns = [
    path('', EnergyBalanceListCreateView.as_view(), name='energy-list-create'),
    path('upload/', EnergyBalanceUploadView.as_view(), name='energy-upload'),
]

