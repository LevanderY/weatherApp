import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import cityForm

def index(request):
    appid = '3777730a40e834273d26a50193921b5d'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    
    err_msg = ''
    message = ''
    message_class = ''

    if(request.method == 'POST'):
        form = cityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            exis_city_count = City.objects.filter(name=new_city).count()

            if exis_city_count == 0:
                res = requests.get(url.format(new_city)).json()
                if res['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City like this does not exist!'
            else:
                err_msg = 'City like this already added!'

        if err_msg:
            message = err_msg
            message_class = 'danger'
        else:
            message = 'City added successfuly!'
            message_class = 'success'

    # Очищення форми 
    form = cityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {
        'allInfo' : all_cities,
        'form' : form,
        'message' : message,
        'message_class' : message_class,
    }

    return render(request, 'weather/index.html', context)

def del_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('home')
