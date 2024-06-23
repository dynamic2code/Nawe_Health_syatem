from django.urls import path
from .views import DonorListCreateAPIView, DonorDetailAPIView

urlpatterns = [
    path('', DonorListCreateAPIView.as_view()),
    path('<int:pk>/', DonorDetailAPIView.as_view()),
]
