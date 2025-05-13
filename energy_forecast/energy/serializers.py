from rest_framework import serializers
from .models import EnergyBalance


class EnergyBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyBalance
        fields = '__all__'
