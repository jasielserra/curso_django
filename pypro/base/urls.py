from django.urls import path
from pypro.base.views import home

app_name = 'aperitivos'
urlpatterns = [
    path('', home, name='home'),
]