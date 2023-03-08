
from tkinter import *
import math as m
root = Tk()
root.title("Scentific Calculator")
Entries = Entry(root, width = 50, borderwidth = 5, relief = RIDGE, fg = "white", bg = "black" )
Entries.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 15)

def click(print) :
    value = Entries.get()
    Entries.delete(0, END)
    Entries.insert(0, value+print)
    return
def secntific(res) :
    key = res.widget
    text = key['text']
    num = Entries.get()
    result = ''
    if text == ',,,' :
        result = str(m.degrees(float(num)))
    elif text == 'sin' :
        result = str(m.sin(float(num)))
    elif text == 'cos' :
        result = str(m.cos(float(num)))
    elif text == 'tan' :
        result = str(m.tan(float(num)))
    elif text == 'lg' :
        result = str(m.log10(float(num)))
    elif text == 'ln' :
        result = str(m.log(float(num)))
    elif text == '√' :
        result = str(m.sqrt(float(num)))
    elif text == 'x!' :
        result = str(m.factorial(float(num)))
    elif text == '1/x' :
        result = str(1/(float(num)))
    elif text == 'π' :
        if num == "" :
            result = str(m.pi)
        else :
            result = str(float(num)*m.pi)
    elif text == 'e' :
        if num == "" :
            result = str(m.e)
        else :
            result = str(m.e**float(num))
    
                       


    Entries.delete(0, END)
    Entries.insert(0, result)


def clear() :
    Entries.delete(0, END)
    return
def BackSpc() :
    current = Entries.get()
    length = len(current)-1
    Entries.delete(length, END)
    
    
def evaluate() :
    answer = Entries.get()
    answer = eval(answer)
    Entries.delete(0,END)
    Entries.insert(0, answer)
lg = Button(root, text = "lg", padx = 40, pady = 10, relief = RAISED, bg = "blue")
lg.bind("<Button-1>",secntific)
ln = Button(root, text = "ln", padx = 47, pady = 10, relief = RAISED, bg = "blue" )
ln.bind("<Button-1>",secntific)
Qos = Button(root, text = "(", padx = 50, pady = 10, relief = RAISED, bg = "blue",  command = lambda : click("("))
Qos0 = Button(root, text = ")", padx = 51, pady = 10, relief = RAISED, bg = "blue",  command = lambda : click(")"))
dott = Button(root, text = ".", padx = 35, pady = 10, relief = RAISED, bg = "blue", command = lambda : click(".") )
exp = Button(root, text = "^", padx = 40, pady = 10, relief = RAISED, bg = "blue",  command = lambda : click("^"))
degbu = Button(root, text = ",,,", padx = 47, pady = 10, relief = RAISED, bg = "blue")
degbu.bind("<Button-1>",secntific)
sinbu = Button(root, text = "sin",padx = 45, pady = 10, relief = RAISED, bg = "blue")
sinbu.bind("<Button-1>",secntific)
cosbu = Button(root, text = "cos",padx = 44, pady = 10, relief = RAISED, bg = "blue")
cosbu.bind("<Button-1>",secntific)
tanbu = Button(root, text = "tan",padx = 29, pady = 10, relief = RAISED, bg = "blue")
tanbu.bind("<Button-1>",secntific)
sqrtbu = Button(root, text = "√",padx = 40, pady = 10, relief = RAISED, bg = "blue", command = lambda : click("√"))
sqrtbu.bind("<Button-1>",secntific)
cbu = Button(root, text = "C", padx = 47, pady = 10, relief = RAISED, bg = "red", command = lambda : clear())
cbu.bind("<Button-1>",secntific)
bkspcbu = Button(root, text = "Bksp", padx = 42, pady = 10, relief = RAISED, bg = "red")
bkspcbu.bind("<Button-1>",secntific)
modbu = Button(root, text = "%", padx = 47.5, pady = 10, relief = RAISED, bg = "blue", command = lambda : click("%"))
divbu = Button(root, text = "/", padx = 35, pady = 10, relief = RAISED, bg = "blue", command = lambda : click("/"))
factbu = Button(root, text = "x!", padx = 40, pady = 10, relief = RAISED, bg = "blue", command = lambda : click("x!"))
factbu.bind("<Button-1>",secntific)
sevenbu = Button(root, text = "7", padx = 47, pady = 10, relief = RAISED, bg = "gray", command = lambda : click("7"))
eightbu = Button(root, text = "8", padx = 50, pady = 10, relief = RAISED, bg = "gray", command = lambda : click("8"))
ninebu = Button(root, text = "9", padx = 50, pady = 10, relief = RAISED, bg = "gray", command = lambda : click("9"))
multibu = Button(root, text = "*", padx = 35, pady = 10, relief = RAISED, bg = "blue", command = lambda : click("*"))
fracbu = Button(root, text = "1/x", padx = 35, pady = 10, relief = RAISED, bg = "blue")
fracbu.bind("<Button-1>",secntific)
fourbu = Button(root, text = "4", padx = 47, pady = 10, relief = RAISED, bg = "gray", command = lambda : click("4"))
fivebu = Button(root, text = "5", padx = 50, pady = 10, relief = RAISED, bg = "gray", command = lambda : click("5"))
sixbu = Button(root, text = "6", padx = 50, pady = 10, relief = RAISED, bg = "gray", command = lambda : click("6"))
minusbu = Button(root, text = "-", padx = 35, pady = 10, relief = RAISED, bg = "blue", command = lambda : click("-"))
pibu = Button(root, text = "π", padx = 40, pady = 10, relief = RAISED, bg = "blue")
pibu.bind("<Button-1>",secntific)
onebu = Button(root, text = "1", padx = 47, pady = 10, relief = RAISED, bg = "gray", command = lambda : click("1"))
twobu = Button(root, text = "2", padx = 50, pady = 10, relief = RAISED, bg = "gray", command = lambda : click("2"))
threebu = Button(root, text = "3", padx = 50, pady = 10, relief = RAISED, bg = "gray", command = lambda : click("3"))
plusbu = Button(root, text = "+", padx = 35, pady = 10, relief = RAISED, bg = "blue", command = lambda : click("+"))
ebu = Button(root, text = "e", padx = 50, pady = 10, relief = RAISED, bg = "blue")
ebu.bind("<Button-1>",secntific)
zerobu = Button(root, text = "0", padx = 50, pady = 10, relief = RAISED, bg = "gray", command = lambda: click("0"))
equalbu = Button(root, text = "=", padx = 50, pady = 10, relief = RAISED, bg = "yellow", command = lambda : evaluate())

lg.grid(row = 1, column = 0)
ln.grid(row = 1, column = 1)
Qos.grid(row = 1, column = 2)
Qos0.grid(row = 1, column = 3)
dott.grid(row = 1, column = 4)

exp.grid(row = 2, column = 0)
degbu.grid(row = 2, column = 1)
sinbu.grid(row = 2, column = 2)
cosbu.grid(row = 2, column = 3)
tanbu.grid(row = 2, column = 4)

sqrtbu.grid(row = 3, column = 0)
cbu.grid(row = 3, column = 1)
bkspcbu.grid(row = 3, column = 2)
modbu.grid(row = 3, column = 3)
divbu.grid(row = 3, column = 4)

factbu.grid(row = 4, column = 0)
sevenbu.grid(row = 4, column = 1)
eightbu.grid(row = 4, column = 2)
ninebu.grid(row = 4, column = 3)
multibu.grid(row = 4, column = 4)


fracbu.grid(row = 5, column = 0)
fourbu.grid(row = 5, column = 1)
fivebu.grid(row = 5, column = 2)
sixbu.grid(row = 5, column = 3)
minusbu.grid(row = 5, column = 4)

pibu.grid(row = 6, column = 0 )
onebu.grid(row = 6, column = 1 )
twobu.grid(row = 6, column = 2 )
threebu.grid(row = 6, column = 3)
plusbu.grid(row = 6, column = 4)

ebu.grid(row = 7, column = 1)
zerobu.grid(row = 7, column = 2)
equalbu.grid(row = 7, column = 3)

root.mainloop()











