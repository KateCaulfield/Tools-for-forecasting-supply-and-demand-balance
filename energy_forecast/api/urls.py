from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('energy/', include('energy.urls')),
    path('forecast/', include('forecast.urls')),
    

]
