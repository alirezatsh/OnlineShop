from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class TokenVerifyView(APIView):
    """
    this view is for verifying the tokens using GET request
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        auth = JWTAuthentication()

        try:
            token = request.headers.get('Authorization').split(' ')[1]
            auth.get_validated_token(token)
            return Response({"message": "token is valid"}, status=status.HTTP_200_OK)
        except (InvalidToken, AttributeError):
            return Response({"message": "token is not valid or the user does not exist"}, status=status.HTTP_401_UNAUTHORIZED)