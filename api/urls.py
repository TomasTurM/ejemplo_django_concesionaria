from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListAuto.as_view()),
    path('<int:pk>/', views.DetailAuto.as_view()),
]