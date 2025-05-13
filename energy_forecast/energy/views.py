from rest_framework import generics
from .models import EnergyBalance
from .serializers import EnergyBalanceSerializer
from rest_framework.permissions import IsAuthenticated

class EnergyBalanceListCreateView(generics.ListCreateAPIView):
    queryset = EnergyBalance.objects.all()
    serializer_class = EnergyBalanceSerializer
    permission_classes = [IsAuthenticated]

import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.files.storage import default_storage

class EnergyBalanceUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        excel_file = request.FILES.get('file')
        if not excel_file:
            return Response({"error": "Файл не передан"}, status=400)

        file_path = default_storage.save(f'temp/{excel_file.name}', excel_file)
        df = pd.read_excel(default_storage.path(file_path))

        required_columns = {
            'resource', 'year', 'city', 'production',
            'import_value', 'export_value', 'consumption',
            'price_per_unit', 'revenue', 'generation_type'
        }

        if not required_columns.issubset(set(df.columns)):
            return Response({"error": "Неверная структура файла"}, status=400)

        records_created = 0
        for _, row in df.iterrows():
            obj, created = EnergyBalance.objects.update_or_create(
                resource=row['resource'],
                year=row['year'],
                city=row['city'],
                defaults={
                    'production': row['production'],
                    'import_value': row['import_value'],
                    'export_value': row['export_value'],
                    'consumption': row['consumption'],
                    'price_per_unit': row['price_per_unit'],
                    'revenue': row['revenue'],
                    'city': row['city'],
                    'generation_type': row['generation_type'],
                }
            )
            if created:
                records_created += 1

        return Response({"message": f"Загружено записей: {records_created}"}, status=status.HTTP_201_CREATED)
