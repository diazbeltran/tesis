from datos.models import Accidente
from django.shortcuts import render_to_response

def lista_accidentes(request):
	accidente = Accidente.objects.all()
	return render_to_response('lista_accidentes.html',{'lista':accidentes})
	
