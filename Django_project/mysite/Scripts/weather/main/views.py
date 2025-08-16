from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'd7e98b723cb84a2b868b02c077fa399c'
  # replace with your actual API key
        source = urllib.request.urlopen(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'K',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
    else:
        data = {}
    return render(request, "main/index.html", data)