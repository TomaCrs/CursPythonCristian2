from django.urls import path

from ap1 import views

app_name = 'ap1'

urlpatterns = [
    path('', views.RetetaView.as_view(), name='lista_retete'),
    path('istoric/', views.IstoricView.as_view(), name='istoric_retete'),
    path('adaugare/', views.CreateRetetaView.as_view(), name='adaugare'),
    path('<int:pk>/modifica/', views.UpdateRetetaView.as_view(), name='modifica'),
    path('<int:pk>/dezactiveaza', views.deactivate_reteta, name='dezactiveaza'),
    path('<int:pk>/activeaza', views.activate_reteta, name='activeaza'),
    path('<int:pk>/stergere', views.delete_reteta, name='stergere'),
]