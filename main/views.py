from django.shortcuts import render
from Other_functions.functions import doen
from django.contrib.auth import authenticate, login

def mainpageview(request):
	if request.method=="POST":
		form = auth_form(request.POST)
		if form.is_valid():
			user = authenticate(request, username=doen(form.cleaned_data.get('username'),True), password=doen(form.cleaned_data.get('password'),True))
			if user is not None:
				login(request, user)
			else:
				#another code
		else:
			#another code
	else:
		form = auth_form(request.GET)
		return render(request,'mainpage',{'form':form})