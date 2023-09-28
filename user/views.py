"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthBasicSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer




class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user