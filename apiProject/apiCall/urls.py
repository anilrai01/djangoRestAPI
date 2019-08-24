from django.urls import path

from . import views 

urlpatterns = [
    path('', views.GridList.as_view()),
    path('<int:pk>/', views.GridDetail.as_view()),
]
