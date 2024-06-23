from django.urls import path
from .views import DonationListCreateAPIView, DonationDetailAPIView

urlpatterns = [
    path('', DonationListCreateAPIView.as_view()),
    path('<int:pk>/', DonationDetailAPIView.as_view()),
]
