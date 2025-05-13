from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from energy.models import EnergyBalance
from .prophet_model import run_prophet_forecast
from .arima_model import run_arima_forecast
from .random_forest_model import run_rf_forecast
from .linear_model import run_linear_regression
from .lstm_model import run_lstm_forecast


class ForecastView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        resource = request.query_params.get('resource')
        model_name = request.query_params.get('model', 'prophet')
        city = request.query_params.get('city')

        if not resource:
            return Response({'error': 'Укажите параметр resource'}, status=400)

        queryset = EnergyBalance.objects.filter(resource=resource)

        if city and city.lower() != 'все':
            queryset = queryset.filter(city=city)

        data = queryset.values(
            'year', 'consumption', 'production', 'import_value', 'export_value'
        ).order_by('year')

        if not data.exists():
            return Response({'error': 'Нет данных по данному ресурсу'}, status=404)

        print("MODEL DEBUG:", model_name)

        try:
            if model_name == 'prophet':
                forecast, metrics = run_prophet_forecast(data)
            elif model_name == 'arima':
                forecast, metrics = run_arima_forecast(data)
            elif model_name == 'rf':
                forecast, metrics = run_rf_forecast(data)
            elif model_name == 'linear':
                forecast, metrics = run_linear_regression(data)
            elif model_name == 'lstm':
                forecast, metrics = run_lstm_forecast(data)
            else:
                return Response({'error': 'Неизвестная модель'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

        return Response({
            'resource': resource,
            'model': model_name,
            'city': city or 'Все',
            'forecast': forecast,
            'metrics': metrics
        })
