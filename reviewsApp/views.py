from .models import Review
from .serializers import ReviewSerializer, MailSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from pyBack.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string


class ReviewView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class MailView(APIView):

    serializer_class = MailSerializer

    def post(self, request):
        serializer = MailSerializer(data=request.data)

        if serializer.is_valid():
            send_mail(subject='Sup 2ch',
                      from_email=EMAIL_HOST_USER,
                      message=None,
                      recipient_list=['danilandryushenko34@gmail.com'],
                      html_message=render_to_string('html_message.html', {'hz': serializer.data['message_text']}),
                      fail_silently=False
                      )
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
