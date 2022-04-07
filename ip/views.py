from django.shortcuts import render
import requests
from django.views.generic import TemplateView

class IPView(TemplateView):
    template_name = 'ip/home.html'
    def ip(request):
        response = requests.get('http://demo.ip-api.com/json')
        geodata = response.json()
        return render(request, 'ip/home.html', {
            'city': geodata['city'],
            
            
        }
    )