from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            # default to match order model
            'default_first_name': 'First Name',
            'default_last_name': 'Last Name',
            'default_mobile_number': 'Mobile Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_address_line1': 'Address Line 1',
            'default_address_line2': 'Address Line 2',
            'default_county': 'County, State or Province',
        }

        self.fields['default_mobile_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False