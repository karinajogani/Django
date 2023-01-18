from rest_framework import serializers
from .models import Student
# from  import

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
