from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import permissions
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer




class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

