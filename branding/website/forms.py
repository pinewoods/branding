from django import forms

from django.utils.translation import gettext as _

from .models import Contact

# Create your views here.

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','phone','email','message']

        labels = {
                'name': 'Full Name *',
                'phone': 'Phone',
                'email': 'E-mail *',
                'message':'Message *'
        }
        error_messages = {
            'name': {'required': _("Please, insert your name.")},
            'phone':{'invalid_phone':_("Please, insert only numbers and the + character.")},
            'email': {'required': _("Please, insert an e-mail."), 'invalid': _("Please, insert a valid e-mail.")},
            'message': {'required': _("Your message is empty.")},
        }
