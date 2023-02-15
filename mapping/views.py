from django.http import HttpResponse
from django.shortcuts import render
import folium
from folium.features import LatLngPopup
from jinja2 import Template
from .models import Mapping


class GLatLngPopup(LatLngPopup):
    """
    When one clicks on a Map that contains a LatLngPopup,
    a popup is shown that displays the latitude and longitude of the pointer.

    """
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                function latLngPop(e) {
                data = e.latlng.lat.toFixed(4) + "," + e.latlng.lng.toFixed(4);
                    {{this.get_name()}}
                        .setLatLng(e.latlng)
                        .setContent( "<br /><a href="+data+"> click </a>")
                        .openOn({{this._parent.get_name()}})
                    }
                {{this._parent.get_name()}}.on('click', latLngPop);

            {% endmacro %}
            """)  # noqa

    def __init__(self):
        super(LatLngPopup, self).__init__()
        self._name = 'LatLngPopup'


def home(request):
    points = Mapping.objects.all()
    m = folium.Map(location=[-15.793889, -47.882778], zoom_start=11)

    for point in points:
        coord = (point.latitude, point.longitude)
        folium.Marker(coord, popup=point.name).add_to(m)

    m.add_child(folium.ClickForMarker(popup='Waypoint'))
    m.add_child(GLatLngPopup())

    mapp = m._repr_html_()

    return render(request, 'index.html', context={'map': mapp})


def create(request):
    # import ipdb;ipdb.set_trace()
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        expiration_date = request.POST.get('expiration_date')

        new_mark = Mapping.objects.create(
            name=name,
            latitude=latitude,
            longitude=longitude,
            expiration_date=expiration_date
        )
        new_mark.save()

        return HttpResponse('Marcação criada com sucesso!')
