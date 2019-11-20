from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlenaView.as_view(), name = 'getHtml'),
]