import PySimpleGUI as sg
from application.bll.controllers.customer_controller import get_all_customer

sg.theme('Dark Grey 11')

order_data = [['Test', 'Test', 'test', 'test', 'test'],
              ['Test', 'Test', 'test', 'test', 'test'],
              ['Test', 'Test', 'test', 'test', 'test']]

inventory_data = [['Test', 'Test', 'test', 'test', 'test'],
              ['Test', 'Test', 'test', 'test', 'test'],
              ['Test', 'Test', 'test', 'test', 'test']]

temp = [['Test', 'Test', 'test', 'test', 'test'],
        ['Test', 'Test', 'test', 'test', 'test'],
        ['Test', 'Test', 'test', 'test', 'test']]

# Text1
h1 = {'size': (20, 1),
      'justification': 'c',
      'font': ('BioRhyme', 28, 'bold')}

h2 = {'size': (11, 1),
      'font': ("Sora", 14, 'bold')}

p = {'font': ("Sora", 14),
     'justification': 'c'}

# Buttons
button1 = {'size': (12, 1),
           'font': ('Sora SemiBold', 14, 'bold')}

button2 = {'font': ('Sora SemiBold', 14)}

filler = {'size': (10, 1), 'font': ('Sora SemiBold', 12, 'bold')}

# Window template
wdw = {'finalize': 'True',
       'size': (1800, 900),
       'resizable': 'True',
       'element_justification': 'c'}

# Table preset
table = {'auto_size_columns': 'True',
         'num_rows': min(15, 25),
         'font': ("Sora", 12),
         'justification': 'c',
         'expand_y': 'True',
         'expand_x': 'True',
         'alternating_row_color': '#222831'}

