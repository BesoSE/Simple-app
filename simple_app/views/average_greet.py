from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from simple_app.serializers.average_greet import NumberSerializer, GreetSerializer


class AverageView(GenericAPIView):
    serializer_class = NumberSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"average": serializer.average_number()}, status=status.HTTP_200_OK)


class GreetView(GenericAPIView):
    serializer_class = GreetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"greeting": serializer.greeting()}, status=status.HTTP_200_OK)
