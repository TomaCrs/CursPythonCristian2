from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('new account', views.CreateNewAccountView.as_view(), name='utilizator_nou'),
    path('user_list', views.ListOfUserView.as_view(), name='listare_utilizatori'),
    path('<int:pk>/editare/', views.UpdateUserView.as_view(), name = 'editare_utilizator'),
    path('<int:pk>/stergere', views.delete_location, name='stergere'),
]