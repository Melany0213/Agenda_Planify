from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Pt_FTL
from ..serializers.serializer_pt_ftl import Pt_FTL_Serializer

# Vistas Genéricas DRF
class Pt_FTLList(ListCreateAPIView):
    queryset = Pt_FTL.objects.all()
    serializer_class = Pt_FTL_Serializer

class Pt_FTLDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pt_FTL.objects.all()
    serializer_class = Pt_FTL_Serializer
