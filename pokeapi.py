import PySimpleGUI as sg

import requests 
import json 

response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

js=response.json()

def jPrint(obj):
    text = json.dumps(obj, sort_keys= True, indent= 4)
    print(text)

jPrint(js)


sg.theme('Reddit')

col1=[
        [sg.Text('dummy')]
    ]
#terminal
col2=[
        [sg.Output(size=(60,15))]
    ]