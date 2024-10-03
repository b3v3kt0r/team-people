from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from user.models import User
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
