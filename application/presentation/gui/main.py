from temp_functions import *
from main_menu import *
from customer_windows import *
from order_windows import *
from inventory_windows import *

'''
Main window for the GUI, containing the Event-handler-loop.
In order to run the GUI, run this file.

Variables = edit settings for the windows and buttons. (Fonts etc.)
'''


def event_handler():
    # Windows:
    main_screen, customer_screen, orders_screen, inventory_screen, \
        add_customer_screen, edit_customer_screen = \
        main_menu(), None, None, None, None, None

    selected_row = None

    # Event handler loop
    while True:
        # prepare all windows
        window, event, values = sg.read_all_windows()

        # MAIN MENU SCREEN
        if event == sg.WIN_CLOSED or None and window == main_screen:
            break
        # Customers - button
        if event == 'Customers' and not customer_screen:
            main_screen.close()
            customer_screen = customer_window()
        # Orders - button
        if event == 'Orders' and not orders_screen:
            main_screen.close()
            orders_screen = orders_window()
        # Inventory - button
        if event == 'Inventory' and not inventory_screen:
            main_screen.close()
            inventory_screen = inventory_window()

        # Customer Screen buttons
        if window == customer_screen:
            if event in '-TABLE-':
                selected_row = values['-TABLE-'][0]

            if event in (sg.Button, 'Add Customer'):
                add_customer_screen = add_customer_window()

            elif event in (sg.Button, 'Remove Customer') and selected_row is not None:
                data.pop(selected_row)
                customer_screen = customer_window()

            elif event in (sg.Button, 'Edit Customer') and selected_row is not None:
                edit_customer_screen = edit_customer_window(data[selected_row])

            elif event in (sg.Button, 'Back'):
                customer_screen.close()
                customer_screen = None
                main_screen = main_menu()

        # ADD CUSTOMER SCREEN
        if window == add_customer_screen:
            # Add Customer
            if event in (sg.Button, '-ADD-'):
                output = [str(values[key]) for key in values]
                add_customer(output)

                add_customer_screen.close()
                customer_screen = customer_window()

            # Cancel
            elif event in (sg.Button, 'Cancel'):
                add_customer_screen.close()

        # EDIT CUSTOMER WINDOW
        if window == edit_customer_screen:
            if event in (sg.Button, '-EDIT-'):
                output = [str(values[key]) for key in values]
                edit_customer(selected_row, output)

                edit_customer_screen.close()
                customer_screen = customer_window()

            elif event in (sg.Button, 'Cancel'):
                edit_customer_screen.close()

        if window == inventory_screen:
            if event in (sg.Button, "Back"):
                main_screen.un_hide()
                inventory_screen.close()


if __name__ == '__main__':
    event_handler()
