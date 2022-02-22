from django.urls import path

from instagram import views

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
]