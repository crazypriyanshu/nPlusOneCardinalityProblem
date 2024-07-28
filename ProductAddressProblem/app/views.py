from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import User, ShippingAddress
from .serializers import UserSerializer, CreateShippingAddressSerializer, ShippingAddressSerializer
from django.shortcuts import get_object_or_404


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShippingAddressListCreateAPIView(ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer


    def post(self, request, user_id):
        try:
            user = get_object_or_404(User, pk=user_id)
            serialized = CreateShippingAddressSerializer(data=request.data)
            if not serialized.is_valid():
                return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
            shipping_address = ShippingAddress(
                city=serialized.data['city'],
                state=serialized.data['state'],
                zip=serialized.data['zip'],
                street=serialized.data['street'],
                country=serialized.data['country'],
            )
            shipping_address.save(self.request.user)
            return Response(ShippingAddressSerializer(
                shipping_address
            ).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




