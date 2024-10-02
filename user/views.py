from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
