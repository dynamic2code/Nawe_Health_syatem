from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Donor
from .serializers import DonorSerializer

class DonorListCreateAPIView(APIView):
    def get(self, request):
        donors = Donor.objects.all()
        serializer = DonorSerializer(donors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DonorDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            donor = Donor.objects.get(pk=pk)
        except Donor.DoesNotExist:
            return Response({'message': 'Donor not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DonorSerializer(donor)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            donor = Donor.objects.get(pk=pk)
        except Donor.DoesNotExist:
            return Response({'message': 'Donor not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DonorSerializer(donor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            donor = Donor.objects.get(pk=pk)
        except Donor.DoesNotExist:
            return Response({'message': 'Donor not found'}, status=status.HTTP_404_NOT_FOUND)
        donor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
