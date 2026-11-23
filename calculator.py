from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""

# Update the display
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Evaluate the full expression
def equal():
    global expression
    try:
        exp = expression.replace("^", "**")
        exp = exp.replace("%", "/100")
        result = str(eval(exp))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Clear the screen
def clear():
    global expression
    expression = ""
    equation.set("")

# Undo in the screen
def backspace():
    global expression
    expression = expression[:-1]  
    equation.set(expression)      


# Display screen
equation = StringVar()
entry = Entry(root, textvariable=equation, font=("Arial", 23,"bold"), bd=10, relief=SUNKEN, justify="right",bg="#ecf0f1", fg="#1e1e1e")
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)



# BUTTONS 
btns = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('%', 4, 1), ('^', 4, 2), ('/', 4, 3),
]

for (value, row, col) in btns:
    Button(root, text=value, width=6, height=2, font=("Arial", 16,"bold"),  bg="#3498db", fg="white",  
           activebackground="#3582b5", activeforeground="white",bd=6,relief="raised",
           command=lambda t=value: press(t)).grid(row=row, column=col)

# Clear button
Button(root, text="C", width=6, height=2, font=("Arial", 16,"bold"),bg="#e74c3c", fg="white",bd=6,relief="raised",
       command=clear).grid(row=5, column=0)

# Equal button
Button(root, text="=", width=6, height=2, font=("Arial", 16,"bold"), bg="#2ecc71", fg="white",bd=6,relief="raised",
       command=equal).grid(row=5, column=1)

#Quit button
Button(root,text="Quit",width=6, height=2, font=("Arial", 16,"bold"), bg="#95a5a6", fg="white",bd=6,relief="raised",
       command=root.destroy).grid(row=5,column=3)

#Undo button
Button(root,text="⌫",width=6, height=2, font=("Arial", 16,"bold"), bg="#f1c40f", fg="white",bd=6,relief="raised",
       command=backspace).grid(row=5,column=2)


root.mainloop()