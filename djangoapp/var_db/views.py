from django.shortcuts import render

from django.http import HttpResponse

from .models import Variant

from django.template import loader

def index(request):
	
	latest_variant_list = Variant.objects.order_by('-created_date')[:2]

	template = loader.get_template('var_db/index.html')

	context = {
		'latest_variant_list': latest_variant_list,
	}

	return HttpResponse(template.render(context, request))
