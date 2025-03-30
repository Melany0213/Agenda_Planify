from rest_framework import serializers
from ..models import Pt_FTL

class Pt_FTL_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pt_FTL
        fields = '__all__'
