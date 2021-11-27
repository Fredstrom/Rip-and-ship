import PySimpleGUI as sg

customerbutton = {'size': (10,2), 'font': ('Roboto Mono', 12), 'button_color': ("black", "#F8F8F8")}
orderbutton = {'size': (10,2), 'font': ('Roboto Mono', 12), 'button_color': ("black", "#F8F8F8")}
inventorybutton= {'size': (10,2), 'font': ('Roboto Mono', 12), 'button_color': ("black", "#F8F8F8")}


# allt inuti fönstren

layout = [
    [sg.Text('Rip And Ship AB', size=(50,1), justification='c', background_color="#EDC7E3",
     text_color='black', font=('Franklin Gothic Book', 30, 'bold'))],
    [sg.Text('The worlds greatest search engine for our employees', size=(100,1), justification='c',
             background_color="#EDC7E3",
    text_color='black', font=('Franklin Gothic Book', 15,))],
    [sg.Button('Customer',**customerbutton),
     sg.Button('Order', **orderbutton), sg.Button('Inventory', **inventorybutton)],
]

# skapa fönstret
window = sg.Window('Rip And Ship', layout=layout, background_color="#EDC7E3", size=(700, 700),
                   grab_anywhere=True, element_justification='c')


# event loop för att processa events

while True:
    event, values = window.read()
    if event is None:
        break

window.close()

