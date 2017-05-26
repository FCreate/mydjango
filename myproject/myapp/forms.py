from django import forms
from .models import User
from .models import Buyer
from myapp.models import Product

from django.db.models import Q

class UserForm(forms.ModelForm):
    
    class Meta:
        model=User
        exclude = ()
        
class ProductForm(forms.ModelForm):
    
    class Meta:
        model=Product
        exclude=()

class RegistrationForm(forms.Form):
    username=forms.CharField(label='Username', max_length=80)
    password = forms.CharField(label='Password',widget=forms.PasswordInput, max_length=80)
    first_name = forms.CharField(label='First name', max_length=80)
    last_name = forms.CharField(label='Last name', max_length=80)
    email = forms.CharField(label='Email', max_length=80)
    phone = forms.CharField(label='Phone', max_length=80)
    city=forms.CharField(label='Cty', max_length=80)
    street = forms.CharField(label='Street', max_length=80)
    house=forms.CharField(label='House', max_length=80)
    apartment=forms.CharField(label='Apartment', max_length=80)

    def is_valid(self):

        # run the parent validation first
        valid = super(RegistrationForm, self).is_valid()

        # we're done now if not valid
        if not valid:
            return valid

        # so far so good, get this user based on the username or email
        try:
            user = User.objects.get(
                Q(username=self.cleaned_data['username']) | Q(email=self.cleaned_data['username'])

            )
            self._errors['username'] = 'This username is taken.'
            return False

        # no user with this username or email address
        except User.DoesNotExist:
            return True

class BuyForm(forms.Form):
    text = forms.CharField(label='text', max_length=80)

