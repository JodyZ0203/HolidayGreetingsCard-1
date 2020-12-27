from django import forms

from .models import CardInfo

class CardFields(forms.ModelForm):
    class Meta:
        model = CardInfo
        fields = ('id', 'Holiday_Choice', 'Recipient_Name', 'Recipient_Location','Your_Name')
