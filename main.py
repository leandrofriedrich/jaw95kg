import PySimpleGUI as sg
import keygen
from pygame import mixer

# start the music
mixer.init()
mixer.music.load("unreeeal_superhero_3.mp3")
mixer.music.play()

# define the layout
layout = [[sg.Text("Just another Windows 95 Keygen")], [sg.Text("Generated Key:"), sg.Text('', key='key')], [sg.Button("Generate CD Key"), sg.Button("Generate OEM Key")]]

# Create the window
window = sg.Window("JAW95KG -  Just another Windows 95 Keygen", layout,size=(300, 110))

# Create an event loop
while True:
    event, values = window.read()
    if event == "Generate CD Key":
        cd_key = ""
        cd_key = keygen.cd_keygen_first_block() + '-' + keygen.check_cd_second_block()
        print(cd_key)
        window.FindElement('key').Update(cd_key)
    elif event == "Generate OEM Key":
        oem_key = ""
        oem_key = keygen.oem_keygen_first_block() + '-OEM-' + keygen.check_second_block() + '-' + keygen.oem_keygen_third_block()
        window.FindElement('key').Update(oem_key)
        print(oem_key)
    elif event == "OK" or event == sg.WIN_CLOSED:
        quit()
