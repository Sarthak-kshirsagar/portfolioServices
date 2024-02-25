from rest_framework import generics
from .models import Email
from .serializers import EmailSerializer
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status

class SendEmailView(generics.CreateAPIView):
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        recipient = serializer.validated_data['recipient']
        message = serializer.validated_data['message']

        send_mail(
            'Subject',
            message,
            'your-email@gmail.com',
            [recipient],
            fail_silently=False,
        )

        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Email sent successfully'}, status=status.HTTP_201_CREATED)
