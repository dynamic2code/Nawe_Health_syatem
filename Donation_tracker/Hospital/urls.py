from django.urls import path
from .views import HospitalListCreateAPIView, HospitalDetailAPIView

urlpatterns = [
    path('', HospitalListCreateAPIView.as_view()),
    path('<int:pk>/', HospitalDetailAPIView.as_view()),
]
