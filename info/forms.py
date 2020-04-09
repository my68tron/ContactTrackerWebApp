from django import forms


class SearchForm(forms.Form):
	search_text = forms.IntegerField()



# class EndUserRegistrationForm(forms.ModelForm):
# 	# meta class
# 	class Meta:
# 		model = EndUserProfile
# 		fields = ('full_name', 'mob_no', 'pin_code')



class AdminLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

