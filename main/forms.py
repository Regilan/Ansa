from django import forms

class auth_form(forms.Form):
	username = forms.CharField(label='Username', max_length=70,required=True)
	password = forms.CharField(label='Password', max_length=70, widgets=forms.PasswordInput,required=True)