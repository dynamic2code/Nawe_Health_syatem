from django.urls import path
from .views import AppointmentListCreateAPIView, AppointmentDetailAPIView

urlpatterns = [
    path('', AppointmentListCreateAPIView.as_view()),
    path('<int:pk>/', AppointmentDetailAPIView.as_view()),
]
