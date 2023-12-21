from rest_framework import serializers
from rest_framework.fields import ListField, FloatField


class NumberSerializer(serializers.Serializer):
    numbers = ListField(child=FloatField())

    def average_number(self):
        numbers = self.validated_data.get("numbers")
        if numbers:
            return sum(numbers) / len(numbers)
        raise serializers.ValidationError({'message': 'Please provide a list of numbers.'})


class GreetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    def greeting(self):
        name = self.validated_data.get("name")
        return f"Hi {name}, how are you?"
