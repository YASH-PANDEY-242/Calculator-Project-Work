import tkinter #for GUI
import math 

button_values = [   #structure of the calc
    ["sin", "cos", "tan", "log"], 
    ["ln", "π", "e", "^"],
    ["(", ")", "n!", "√"],
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "ANS", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]  #operators
top_symbols = ["AC", "+/-", "%"]  #functions
scientific_symbols = ["sin", "cos", "tan", "log", "ln", "π", "e", "^", "(", ")", "n!", "√", "ANS"]  #scientific functions

row_count= len(button_values) #8
column_count= len(button_values[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray="#505050"
color_orange="#FF9500"
color_white="white"
color_blue="#007AFF"
color_green="#34C759"

#window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame , text="0", font = ("Times New Roman",50), background=color_black,
                      foreground=color_white, anchor = 'e', width=column_count+4, height=2)
label.grid(row=0,column=0, columnspan=column_count, sticky = "we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Times New Roman",20),
                                width=column_count+2, height=1,
                                 command = lambda value = value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        elif value in scientific_symbols:
            button.config(foreground=color_white, background=color_blue)
        else:
            button.config(foreground=color_white, background=color_dark_gray)

        button.grid(row=row+1, column= column)
frame.pack()
# operations 
A = "0"
operator = None
B = None
last_answer = 0
expression = ""

def clear_all():
    global A, B, operator, expression
    A = "0"
    operator = None
    B = None
    expression = ""

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global right_symbols, top_symbols, scientific_symbols, label, A, B, operator, last_answer, expression

    if value in right_symbols:
        if value == '=':
            try:
                if expression:
                    # Evaluate the full expression
                    expr = expression.replace('×', '*').replace('÷', '/').replace('^', '**').replace('π', str(math.pi)).replace('e', str(math.e))
                    result = eval(expr)
                    label['text'] = remove_zero_decimal(result)
                    last_answer = result
                    expression = ""
                elif A is not None and operator is not None:
                    B = label['text']
                    numA = float(A)
                    numB = float(B)
                    
                    if operator == '+':
                        label['text'] = remove_zero_decimal(numA + numB)
                    elif operator == '-':
                        label['text'] = remove_zero_decimal(numA - numB)
                    elif operator == '×':
                        label['text'] = remove_zero_decimal(numA * numB)
                    elif operator == '÷':
                        label['text'] = remove_zero_decimal(numA / numB)

                    clear_all()
            except ZeroDivisionError:
                label['text'] = "Error"
                clear_all()
        
        elif value in '+-×÷':
            if operator is None:
                A = label['text']
                label['text'] = '0'
                B = '0'

            operator = value
    elif value in top_symbols:
        if value == 'AC':
            clear_all()
            label['text']= '0'
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%": 
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    elif value in scientific_symbols:
        current = float(label['text'])
        
        if value == 'sin':
            result = math.sin(math.radians(current))
            label['text'] = remove_zero_decimal(result)
        elif value == 'cos':
            result = math.cos(math.radians(current))
            label['text'] = remove_zero_decimal(result)
        elif value == 'tan':
            result = math.tan(math.radians(current))
            label['text'] = remove_zero_decimal(result)
        elif value == 'log':
            result = math.log10(current)
            label['text'] = remove_zero_decimal(result)
        elif value == 'ln':
            result = math.log(current)
            label['text'] = remove_zero_decimal(result)
        elif value == 'π':
            label['text'] = remove_zero_decimal(math.pi)
        elif value == 'e':
            label['text'] = remove_zero_decimal(math.e)
        elif value == 'n!':
            result = math.factorial(int(current))
            label['text'] = remove_zero_decimal(result)
        elif value == '√':
            result = math.sqrt(current)
            label['text'] = remove_zero_decimal(result)
        elif value == '^':
            expression += str(current) + '**'
            label['text'] = '0'
        elif value == '(':
            expression += '('
        elif value == ')':
            expression += ')'
        elif value == 'ANS':
            label['text'] = remove_zero_decimal(last_answer)
    else: #for digit
        if value == '.':
            if value not in label['text']:
                label['text'] += value
        elif value in '0123456789':
            if label['text']== '0':
                label['text'] = value
            else:
                label['text'] += value #replace 
#window to the centre
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_width()
screen_height = window.winfo_height()

window_x = int((screen_width/2 ) -(window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#formaat " (w)*(h) + (x)+(y) 
window.geometry(f"{window_width}x{window_height}+{ window_x}+{window_y}")
window.mainloop()
