import tkinter as tk
from PIL import Image, ImageTk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("CalculatorTechnicalExercise")
        master.configure(bg='#ffffff')

        # create display
        self.display = tk.Entry(master, width=25, font=('Arial', 16), bg='#ffffff', fg='#ff0000')
        self.display.grid(row=0, column=0, columnspan=4, pady=5)
        root.resizable(width=False, height=False)  # This prevents the window from being resized

        # create buttons
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3, bg='#ff0000', fg='#ffffff')

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3, bg='#ff0000', fg='#ffffff')

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3, bg='#ff0000', fg='#ffffff')

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('C', 4, 2, bg='#ff0000', fg='#ffffff')
        self.create_button('+', 4, 3, bg='#ff0000', fg='#ffffff')

        self.create_button('=', 5, 0, columnspan=4, bg='#ff0000', fg='#ffffff')


        #BIDMAS buttons
        self.create_button('(', 1, 4, bg='#ff0000', fg='#ffffff')
        self.create_button(')', 1, 5, bg='#ff0000', fg='#ffffff')
        self.create_button('**2', 2, 4, bg='#ff0000', fg='#ffffff')  # Squared
        self.create_button('**3', 2, 5, bg='#ff0000', fg='#ffffff')  # Cubed



        # create conversion buttons
        self.create_conversion_button('Kilos to Stone', 6, 0)
        self.create_conversion_button('Stone to Kilos', 6, 1)
        self.create_conversion_button('Gigabytes to bytes', 6, 2)
        self.create_conversion_button('Bytes to Gigabytes', 6, 3)
        self.create_conversion_button('Inches to Centimetres', 7, 0)
        self.create_conversion_button('Centimetres to Inches', 7, 1)
        self.create_conversion_button('Days to Seconds', 7, 2)
        self.create_conversion_button('Seconds to Days', 7, 3)

        self.create_conversion_button('Decimal', 8, 0)
        self.create_conversion_button('Binary', 8, 1)
        self.create_conversion_button('Octal', 8, 2)
        self.create_conversion_button('Hexidecimal', 8, 3)



        #history

        self.num1 = None
        self.operator = None
        self.input_field_value = tk.StringVar()
        self.history = []



    def create_button(self, text, row, col, columnspan=1, padx=5, pady=5, bg='#ffffff', fg='#ff0000'):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16), command=lambda: self.button_click(text), bg=bg, fg=fg)
        button.grid(row=row, column=col, columnspan=columnspan, padx=padx, pady=pady)

    def create_conversion_button(self, text, row, col, columnspan=1, padx=5, pady=5, bg='#ffffff', fg='#0000ff'):
        button = tk.Button(self.master, text=text, font=('Arial', 10), command=lambda: self.conversion_click(text), bg=bg, fg=fg)
        button.grid(row=row, column=col, columnspan=columnspan, padx=padx, pady=pady)



    def button_click(self, text):
        if text == 'C':
            self.display.delete(0, tk.END)
        elif text == '=':
            try:
                result = str(eval(self.display.get()))
            except:
                result = 'Error'
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        else:
            self.display.insert(tk.END, text)

    def conversion_click(self, text):
        value = self.display.get()
        try:
            if text == 'Kilos to Stone':
                result = float(value) * 0.157473
            elif text == 'Stone to Kilos':
                result = float(value) * 6.35029
            elif text == 'Gigabytes to bytes':
                result = float(value) * 1000000000
            elif text == 'Bytes to Gigabytes':
                result = float(value) / 1000000000
            elif text == 'Inches to Centimetres':
                result = float(value) * 2.54
            elif text == 'Centimetres to Inches':
                result = float(value) / 2.54
            elif text == 'Days to Seconds':
                result = float(value) * 86400
            elif text == 'Seconds to Days':
                result = float(value) / 86400
            elif text == 'Decimal':
                result = decimal(int(value))
            elif text == 'Binary':
                result = bin(int(value))
            elif text == 'Octal':
                result = oct(int(value))
            elif text == 'Hexidecimal':
                result = hex(int(value))
            else:
                result = 'Error'
        except:
            result = 'Error'
        self.display.delete(0, tk.END)
        self.display.insert(0, result)


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

