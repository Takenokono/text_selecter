# 参考
# 1. https://qiita.com/KatsunoriNakamura/items/376da645e52f7ef7f9ef

import PySimpleGUI as sg
import random


# テーマ決め
sg.theme('DarkAmber') 

font = ('Arial', 20)

# All the stuff inside your window.
layout = [  [sg.Text('Enter your text',font=font)],
            [sg.Multiline(size=(50,10),key='input',font=font)],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Text('picked up Topics!!!',font=font)],
            [sg.Multiline(size=(50,10),key='output',font=font)]
            ]


# Create the Window
window = sg.Window('TOPIC selector!', layout, size=(800,800))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    # read contents
    event, values = window.read()
    # Cancel all
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    # read contents
    multiline_text = values['input']
    input_lines = multiline_text.split('\n')
    # pick up one topic
    output_line = input_lines[random.randint(0,len(input_lines)-1)]

    if event == 'Ok':
        window['output'].Update(output_line)

window.close()