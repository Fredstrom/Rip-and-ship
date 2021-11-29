import PySimpleGUI as sg


sg.theme('Dark Grey 11')

data = [['Test', 'Test', 'Test', 'test', 'test'],
        ['Test', 'Test', 'Test', 'test', 'test'],
        ['Test', 'Test', 'Test', 'test', 'test']]

# Text
h1 = {'size': (30, 1),
      'justification': 'c',
      'font': ('Helvetica', 28, 'bold')}

h2 = {'size': (10, 1),
      'font': ("Helvetica", 14, 'bold')}

p = {'font': ("Helvetica", 12),
     'justification': 'c'}

# Buttons
button1 = {'size': (10, 2),
           'font': ('Helvetica', 15, 'bold')}

button2 = {'font': ('Helvetica', 12)}

# Window template
wdw = {'finalize': 'True',
       'size': (900, 600),
       'resizable': 'True',
       'element_justification': 'c'}

# Table preset
table = { 'auto_size_columns': 'False',
          'def_col_width': 12,
          'num_rows': min(25, len(data)),
          'font': "Helvetica",
          'justification': 'c'}

