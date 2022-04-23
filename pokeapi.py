import PySimpleGUI as sg
import sys
import requests 
import json 

    

url= "https://pokeapi.co/api/v2/pokemon"

def getReq(url=url,point=''):
    fstr = f"{url}{point}"
    return requests.get(f"{url}{point}")
    
def jGetReq(url=url,point=''):
    res = getReq(url,point)
    return res.json()

response = getReq()


res=response.json()

def jPrint(obj):
    text = json.dumps(obj, sort_keys= True, indent= 4)
    print("$$$$$$ START $$$$$$")
    print(text)


#interesting themes: Reddit Material4 Python GreenMono HotDogStand Purple SystemDefault1
#print(sg.theme_list())
sg.theme('Python')

#controllers
col1 = [
        [sg.Text(size=(1,1)), sg.InputText(k='-NUM-')],
        [sg.Button('print num', k='-PNUM-')],
        [sg.Button('print', k='-PRINT-')],
        [sg.Button('click', k='-CLICK-')],
        [sg.Button('clear', k='-CLEAR-')],
        [sg.Button('X',k='-CLOSE-')]
    ]

#terminal
col2 = [
        [sg.Output(size=(100,50))]
    ]

#layout
layout = [
    [sg.Column(col1, element_justification='l'),
     sg.Column(col2, element_justification='l')]   
]

#init window 
window = sg.Window(
    title="api",
    layout= layout 
    )



#main loop 
while True: 
    event, val = window.read()
    
    #print api
    if event == '-PRINT-':
        jPrint(res)
        
    if event == '-CLICK-':
        req = jGetReq(url,'/1')
        jPrint(req)
    
    #print entry
    if event == '-PNUM-':
        print(val['-NUM-'])
    
    #clear DOESNT WORK
    if event == '-CLEAR-':
        sg.Output.clear()
    
    #close 
    if event == sg.WIN_CLOSED or event == '-CLOSE-':
        break 
    
window.close()