from rest_framework import serializers
from .models import CardInfo

class CardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardInfo
        fields = ('id', 'Holiday_Choice', 'Recipient_Name', 'Recipient_Location', 'Your_Name', 'created_at')



