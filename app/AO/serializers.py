from rest_framework import serializers
from .models import Appoinment

class AppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appoinment
        fields = ['first_name','last_name','date','time']
