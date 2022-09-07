from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .serializer import ShopSerializer
from rest_framework.permissions import IsAuthenticated

class Shop(ListCreateAPIView):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    