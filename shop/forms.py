from django import forms



class ResevationForm(forms.Form):
    datetime = forms.DateTimeField()
    first_name = forms.CharField(label="First name", max_length=255)
    last_name = forms.CharField(label="Last name", max_length=255)
    phone_number = forms.CharField(max_length=255)

    datetime.widget.attrs.update({'class': 'input'})
    datetime.widget.input_type = 'datetime-local'
    first_name.widget.attrs.update({'class': 'input'})
    last_name.widget.attrs.update({'class': 'input'})
    phone_number.widget.attrs.update({'class': 'input', 'pattern': '[\+\s\d]+'})
    print(vars(phone_number))
