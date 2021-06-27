from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Interior', views.interior, name='interior'),
    path('Exterior', views.exterior, name='exterior'),
    path('tables', views.tables, name='tables'),
]