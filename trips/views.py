# trips/views.py
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from trips.models import GisPoint, Post

@csrf_exempt
def gis(request):
    if request.method == 'POST':
        lat = request.POST.get('lat', '')
        lon = request.POST.get('lon', '')
        item = request.POST.get('item', '')
        gisPoint = GisPoint(lat=lat, lon=lon, item=item)
        gisPoint.save()

        return HttpResponse(status=200)

def hello_world(request):
    return render(request,
                  'hello_world.html',
                  {'current_time': datetime.now()})
