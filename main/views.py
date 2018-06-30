#from django.shortcuts import render
from django.views.generic import TemplateView

class MainPage(TemplateView):
	template_name = "mainpage.html"

	def get_context_data(self, *args, **kwargs):
		context=super(MainPage,self).get_context_data(*args,**kwargs)
		print(context)
		return context