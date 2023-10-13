from django import forms
from django.utils.translation import gettext_lazy as _


class ResevationForm(forms.Form):
    datetime = forms.DateTimeField(label=_('Day and time'))
    first_name = forms.CharField(label=_('First name'), max_length=255)
    last_name = forms.CharField(label=_('Last name'), max_length=255)
    phone_number = forms.CharField(label=_('Phone number'), max_length=255)

    datetime.widget.attrs.update({'class': 'input'})
    datetime.widget.input_type = 'datetime-local'
    first_name.widget.attrs.update({'class': 'input'})
    last_name.widget.attrs.update({'class': 'input'})
    phone_number.widget.attrs.update({'class': 'input',
                                      'pattern': '^\+?[\s\d]{1,30}'})
