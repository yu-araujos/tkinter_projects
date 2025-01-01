from tkinter import *

def button_press(num):
  global equation_text
  equation_text += str(num)
  equation_label.set(equation_text)

def equals():
  global equation_text
  try:
      total = str(eval(equation_text))
      equation_label.set(total)
      equation_text = total
  except (SyntaxError, ZeroDivisionError):
      equation_label.set("error")
      equation_text = ""
  

def clear():
  global equation_text
  equation_text = ""
  equation_label.set("")
  
def key_press(event):
  global equation_text
  if event.keysym == "BackSpace":
      equation_text = equation_text[:-1]
      equation_label.set(equation_text)
  elif event.keysym == "Return":
      equals()
  elif event.char in "0123456789+-*/.":
      button_press(event.char)
      
def create_button(frame, text, row, column, command, width = 9, height = 4, font = 35):
  Button(frame, text=text, height=height, width=width, font=font, command=command).grid(row=row, column=column)

# Window config
window = Tk()
window.title("Calculator")
window.geometry("550x650")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, bg='grey', width=100, height=5)
label.pack()

frame = Frame(window)
frame.pack()

for x in range(10):
    create_button(frame, text=x, row=x // 3, column=x % 3, command=lambda num=x: button_press(num))

operators = {
    "+": (3, 1),
    "-": (3, 2),
    "*": (4, 0),
    "/": (4, 1),
    ".": (4, 2),
    "=": (5, 1),
}

for op, (row, column) in operators.items():
  create_button(frame, text=op, row=row, column=column, command=lambda o=op: button_press(o) if o != "=" else equals())

clear_button = Button(window, text='clear', height=4, width=12, font=35, command=clear)
clear_button.pack()
    
window.bind("<Key>", key_press)
window.mainloop()