from django.shortcuts import render
from .models import TileImage
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Gallery view.")
    facts_list = TileImage.objects.order_by('id').all()
    return render(request, 'gallery/index.html', {'facts_list': facts_list})
