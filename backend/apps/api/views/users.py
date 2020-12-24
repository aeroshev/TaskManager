from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import AllowAny


from api.serializers.users import UserSerializer, UserRegistrationSerializer, UserLoginSerializer
from core.models import TMUser


class UserRegistrationView(GenericViewSet, CreateModelMixin):
    pagination_class = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'message': 'User registered successfully'
        }
        status_code = status.HTTP_201_CREATED

        return Response(response, status_code)


class UserLoginView(GenericViewSet, RetrieveModelMixin):
    pagination_class = (AllowAny,)
    serializer_class = UserLoginSerializer

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': True,
            'message': 'User logged in successfully',
            'token': serializer.data['token']
        }
        status_code = status.HTTP_200_OK

        return Response(response, status_code)


class UserViewSet(ModelViewSet):
    queryset = TMUser.objects.all()
    serializer_class = UserSerializer
