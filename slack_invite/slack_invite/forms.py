from django import forms

class InviteForm(forms.Form):
    email_addr = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email address','id':'email'}), label='')
