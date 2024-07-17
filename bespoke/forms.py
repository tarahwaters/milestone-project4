from django import forms
from .models import Bespoke

class BespokeForm(forms.ModelForm):
    class Meta:
        model = Bespoke
        fields = [
            'name',
            'email',
            'gift_recipient',
            'occasion',
            'wishes',
            'message'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }),
            'gift_recipient': forms.Select(attrs={
                'class': 'form-control'
            }),
            'occasion': forms.Select(attrs={
                'class': 'form-control'
            }),
            'wishes': forms.Select(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': (
                    "Do you have particular 'wishes' in mind, words that you "
                    "would like to be used in the collage (e.g. gratitude / "
                    "adventure / joy / love)? These can be things you want to "
                    "attract for the future, feelings you hope for. If you are "
                    "unsure, let me know + I can come up with ideas for you. "
                    "Also add any extra comments or details here."
                )
            }),
        }