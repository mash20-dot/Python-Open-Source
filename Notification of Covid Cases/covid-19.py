import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data  = r.json()
    text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates",text,duration=100)
        time.sleep(60)
update()


def home(a, b, c):
    return a + b + c

print(home(2, 8, 8))