from django.urls import path

from ap1 import views

app_name = 'ap1'

urlpatterns = [
    path('', views.RetetaView.as_view(), name='lista_retete'),
]