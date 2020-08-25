from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField
from .models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['author_name', 'review_text', 'pub_date']

class MailSerializer(Serializer):
    message_text = CharField()
