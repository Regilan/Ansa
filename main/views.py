from django.shortcuts import render
from Other_functions.functions import doen
from django.contrib.auth import authenticate, login
from main.forms import auth_form
print('inside the view')
def mainpageview(request):
	print('camehere')
	if request.method=="POST":
		form = auth_form(request.POST)
		if form.is_valid():
			user = authenticate(request, username=doen(form.cleaned_data.get('username'),True), password=doen(form.cleaned_data.get('password'),True))
			if user is not None:
				login(request, user)
			else:
				pass
		else:
			pass
	else:
		form = auth_form(request.GET)
		print('Here!')
		return render(request,'main/mainpage.html',{'form':form})