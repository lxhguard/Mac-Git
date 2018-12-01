from django.urls import path
from . import views

urlpatterns = [
    path('1',views.index1, name='1'),
    path('2', views.index2, name='2'),
    path('success', views.success, name="success"),

]