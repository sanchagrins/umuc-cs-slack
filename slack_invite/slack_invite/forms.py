from django import forms

class InviteForm(forms.Form):
    email_addr = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email address','id':'email'}), label='')
    check_terms = forms.BooleanField(label="I agree to the <a link''>Terms and Code of Conduct</a>")
