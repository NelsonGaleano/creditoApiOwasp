# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserDataSerializer
from rest_framework import status

# vista para registrar usuarios
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    user_id = user.id
    serializer = UserDataSerializer(user)

    credito = user.credito

    if credito > 1000000:
        return Response({
            'message': 'tu bandera es flag{3r3sg4n4d04d3lflag}',
            'name': user.name,
            'email': user.email,
            'credito':user.credito
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'credito': credito,
            'name': user.name,
            'email': user.email,
            'user_id': user_id
        }, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)