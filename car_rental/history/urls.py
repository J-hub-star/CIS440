from django.urls import path, include
from . import views

urlpatterns = [
    path('history/', include('history.urls'))
]