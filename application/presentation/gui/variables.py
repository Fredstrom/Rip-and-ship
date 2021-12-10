import PySimpleGUI as sg

sg.theme('Dark Grey 11')

order_data = [['Test', 'Test', 'test', 'test', 'test'],
              ['Test', 'Test', 'test', 'test', 'test'],
              ['Test', 'Test', 'test', 'test', 'test']]

inventory_data = [['Test', 'Test', 'test', 'test', 'test'],
              ['Test', 'Test', 'test', 'test', 'test'],
              ['Test', 'Test', 'test', 'test', 'test']]

data = [['Myra', 'Test', 'Test', 'test', 'test', 'Test', 'test', 'test'],
        ['Meeko', 'Test', 'Test', 'test', 'test', 'Test', 'test'],
        ['Pixel', 'Test', 'Test', 'test', 'test', 'Test', 'test']]

temp = [['Test', 'Test', 'test', 'test', 'test'],
        ['Test', 'Test', 'test', 'test', 'test'],
        ['Test', 'Test', 'test', 'test', 'test']]

# Text1
h1 = {'size': (14, 1),
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
       'size': (1400, 700),
       'resizable': 'True',
       'element_justification': 'c'}

# Table preset
table = {'auto_size_columns': 'True',
         'def_col_width': 12,
         'num_rows': min(25, len(data)),
         'font': ("Sora", 14),
         'justification': 'c',
         'expand_y': 'True',
         'expand_x': 'True',
         'alternating_row_color': '#222831'}

