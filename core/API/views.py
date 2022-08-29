from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from .models import Galary
from .serializers import GalarySerializer


class GalaryApiList(generics.ListCreateAPIView):
    queryset = Galary.objects.all()
    serializer_class = GalarySerializer
    permission_classes = (AllowAny, )


class GalaryApiUpdate(generics.UpdateAPIView):
    queryset = Galary.objects.all()
    serializer_class = GalarySerializer
    permission_classes = (IsAdminUser, )


class GalaryApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Galary.objects.all()
    serializer_class = GalarySerializer
    permission_classes = (IsAdminUser, )


# class RegistrationView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserRegistrationSerializer
#
#     permission_classes = (
#         permissions.AllowAny,
#     )
#
#     def perform_create(self, serializer):
#         user = serializer.save()
#         signals.user_registered.send(sender=self.__class__, user=user, request=self.request)
#         if settings.get('SEND_ACTIVATION_EMAIL'):
#             self.send_activation_email(user)
#         elif settings.get('SEND_CONFIRMATION_EMAIL'):
#             self.send_confirmation_email(user)
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         token = create_token(serializer.data)
#         return Response(data=token, status=status.HTTP_201_CREATED, headers=headers)
#
#     def send_activation_email(self, user):
#         email_factory = utils.UserActivationEmailFactory.from_request(self.request, user=user)
#         email = email_factory.create()
#         email.send()
#
#     def send_confirmation_email(self, user):
#         email_factory = utils.UserConfirmationEmailFactory.from_request(self.request, user=user)
#         email = email_factory.create()
#         email.send()