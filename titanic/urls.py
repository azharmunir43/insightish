from django.urls import path
from titanic import views
app_name = 'titanic'

urlpatterns = [
    path('', views.titanic_home, name='titanic_home'),
    path('predict/', views.titanic_get_result, name='titanic_result')
]