from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Activity
from .serializers.serializer_activity import ActivitySerializer

# Vistas Genéricas DRF
