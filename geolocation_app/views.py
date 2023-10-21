from django.shortcuts import render
from django.http import HttpResponse
from user_agents import parse
import json

# Create your views here.
def index(request):
    return render(request, 'geolocation_app/index.html')

def save_coordinates(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        accuracy = data.get('accuracy')

        ip_address = request.META.get('REMOTE_ADDR', '')
        host = request.META.get('HTTP_HOST', '')
        user_agent_string = request.META.get('HTTP_USER_AGENT', '')
        user_agent = parse(user_agent_string)

        device_details = f'Device: {user_agent.device.family}, OS: {user_agent.os.family}, Browser: {user_agent.browser.family}'


        if latitude is not None and longitude is not None and accuracy is not None:
            with open('coordinates.txt', 'a') as file:
                file.write(f'Latitude: {latitude}, Longitude: {longitude}, Accuracy: {accuracy} meters\n')
                file.write(f'IP Address: {ip_address}, Host: {host}\n')
                file.write(f'{device_details}\n===========================================\n')


            return HttpResponse('Coordinates saved successfully.')

    return HttpResponse('Failed to save coordinates.')
