from django.urls import path

from blog1 import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
]