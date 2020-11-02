#dev shiva gangula.
#intialized 02/11/2020
#last_edited 02/11/2020

from django.shortcuts import render


def home(request):
	return render(request, 'integration/home.html')