from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Flight
from .serializers import FlightSerializer

class FlightDetail(APIView):
    def get(self, request, From, To):
        try:
            flight = Flight.objects.get(From=From, To=To)
            serializer = FlightSerializer(flight)
            return Response(serializer.data)
        except Flight.DoesNotExist:
            return Response({"message": "Flight not found"}, status=status.HTTP_404_NOT_FOUND)
