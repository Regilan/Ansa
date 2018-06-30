from django import forms

class auth_form(forms.Form):
	username = forms.CharField(max_length=70)
	password = forms.CharField(max_length=70, widgets=forms.PasswordInput)