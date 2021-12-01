import PySimpleGUI as sg


sg.theme('Dark Grey 11')

data = [['Myra', 'Test', 'Test', 'test', 'test', 'Test', 'test', 'test'],
        ['Meeko', 'Test', 'Test', 'test', 'test', 'Test', 'test'],
        ['Pixel', 'Test', 'Test', 'test', 'test', 'Test', 'test']]

# Text1
h1 = {'size': (30, 1),
      'justification': 'c',
      'font': ('BioRhyme', 28, 'bold')}

h2 = {'size': (10, 1),
      'font': ("Sora", 14, 'bold')}

p = {'font': ("Sora", 14),
     'justification': 'c'}

# Buttons
button1 = {'size': (12, 1),
           'font': ('Sora SemiBold', 14, 'bold')}

button2 = {'font': ('Sora SemiBold', 14)}

# Window template
wdw = {'finalize': 'True',
       'size': (900, 600),
       'resizable': 'True',
       'element_justification': 'c'}

# Table preset
table = { 'auto_size_columns': 'True',
          'def_col_width': 12,
          'num_rows': min(25, len(data)),
          'font': ("Sora", 14),
          'justification': 'c',
          'expand_y': 'True',
          'expand_x': 'True'}


