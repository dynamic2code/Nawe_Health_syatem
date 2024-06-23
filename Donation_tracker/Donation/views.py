from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Donation
from .serializers import DonationSerializer

class DonationListCreateAPIView(APIView):
    def get(self, request):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DonationDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            donation = Donation.objects.get(pk=pk)
        except Donation.DoesNotExist:
            return Response({'message': 'Donation not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DonationSerializer(donation)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            donation = Donation.objects.get(pk=pk)
        except Donation.DoesNotExist:
            return Response({'message': 'Donation not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DonationSerializer(donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            donation = Donation.objects.get(pk=pk)
        except Donation.DoesNotExist:
            return Response({'message': 'Donation not found'}, status=status.HTTP_404_NOT_FOUND)
        donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
