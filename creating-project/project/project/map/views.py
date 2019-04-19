from django.shortcuts import render
from map.models import Route, Station

# Create your views here.
def stations_views(request):
	context = {}
	context['routes'] = Route.objects.all()
	if request == 'POST':
		route = request.GET['route']
		stations = Station.objects.filter(routes__name=route)
		stations = stations.order_by('longitude')
		st_first = stations.first()
		st_last = stations.last()
		x = (st_first.longitude + st_last.longitude) / 2

		stations = stations.order_by('latitude')
		st_first = stations.first()
		st_last = stations.last()
		y = (st_first.latitude + st_last.latitude ) / 2
		# stations_first = stations.first()
		# stations_last = stations.last()
		# x = (stations_first.longitude + stations_last.longitude)/2
		# y = (stations_first.latitude + stations_last.latitude)/2
		context['stations'] = stations
		context['center'] = {'y': y, 'x': x}
	return render(request, 'stations.html', context)
