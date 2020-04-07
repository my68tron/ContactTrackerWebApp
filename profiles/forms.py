from django import forms
from .models import EndUserProfile
from django.contrib.auth.models import User

class EndUserRegistrationForm(forms.ModelForm):
	# meta class
	class Meta:
		model = EndUserProfile
		fields = ('full_name', 'mob_no', 'pin_code')



class AdminLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)