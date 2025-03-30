from rest_framework import serializers
from ..models import Activity
import calendar
from datetime import datetime

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

    def validate(self, data):
        month = data.get('month')  
        day = data.get('day')  

        if not month or not day:
            raise serializers.ValidationError("El mes y el día son campos obligatorios.")

        # Validar que el mes esté en el rango válido
        if not (1 <= month <= 12):
            raise serializers.ValidationError("El mes debe estar entre 1 y 12.")

        # Obtener el número de días válidos del mes
        year = datetime.now().year
        _, days_in_month = calendar.monthrange(year, month)

        # Validar que el día esté dentro del rango permitido
        if not (1 <= day <= days_in_month):
            raise serializers.ValidationError(
                f"El día {day} no es válido para el mes {calendar.month_name[month]} en el año {year}."
            )

        return data
