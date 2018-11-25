from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name','email','phone_number','message']
        widgets = {
            'name': forms.TextInput (attrs= {'type':'text','class':'form-control','placeholder': 'Name', 'id':'name', 'required data-validation-required-message': 'Please enter your name.'}),
            'email': forms.TextInput (attrs= {'type':'email','class':'form-control','placeholder': 'Email Address', 'id':'email', 'required data-validation-required-message': 'Please enter your Email.'}),
            'phone_number': forms.TextInput (attrs= {'type':'tel','class':'form-control','placeholder': 'Phone Number', 'id':'phone', 'required data-validation-required-message': 'Please enter your Phone Number.'}),
            'message': forms.TextInput (attrs= {'rows': 5,'class':'form-control','placeholder': 'Message', 'id': 'message','required data-validation-required-message': 'Please enter a message.'})
        }