import math
from tkinter import*
root = Tk()
root.title("Simple Calculator")
root.configure(highlightthickness=7,highlightcolor='blue',bg='blue')

e = Entry(root, width=35, borderwidth=5,bg="gray",fg="red",font="5")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
def button_add(number):
    # e.delete(0, END) # deletes the previous
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str(number))

def button_clear():
    e.delete(0, END)
def addind():
    first_num = e.get()
    global f_num
    global math
    math ="Addition"
    f_num = int(first_num)
    e.delete(0, END)

def min():
    first_num = e.get()
    global f_num
    global math
    math ="subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def mut():
    first_num = e.get()
    global f_num
    global math
    math ="multiplicaton"
    f_num = int(first_num)
    e.delete(0, END)  
def div():
    first_num = e.get()
    global f_num
    global math
    math ="Division"
    f_num = int(first_num)
    e.delete(0, END)
def equo():
    second_num = e.get()
    e.delete(0,END)
    if math == "Addition":
        e.insert(0, f_num + int(second_num))
    if math == "Division":
        e.insert(0, f_num / int(second_num))
    if math == "multiplicaton":
        e.insert(0, f_num * int(second_num))

    if math == "subtraction":
        e.insert(0, f_num - int(second_num))   


but_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1),bd="5",bg="purple")
but_2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_add(2),bd="5",bg="purple")
but_3 = Button(root, text="3", padx=40, pady=20, command= lambda: button_add(3),bd="5",bg="purple")
but_4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_add(4),bd="5",bg="purple")
but_5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_add(5),bd="5",bg="purple")
but_6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_add(6),bd="5",bg="purple")
but_7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_add(7),bd="5",bg="purple")
but_8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_add(8),bd="5",bg="purple")
but_9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_add(9),bd="5",bg="purple")
but_0 = Button(root, text="0", padx=40, pady=20, command= lambda: button_add(0),bd="5",bg="purple")


but_min= Button(root, text="-", padx=40, pady=20, command= min,bd="5",bg="gray")
but_mut = Button(root, text="*", padx=40, pady=20, command= mut,bd="5",bg="gray")
but_div = Button(root, text="/", padx=40, pady=20, command=div,bd="5",bg="gray")

but_plus = Button(root, text="+", padx=40, pady=20, command=addind,bd="5",bg="gray")
but_equa = Button(root, text="=", padx=40, pady=20, command=equo,bd="5",bg="gray")
but_clea = Button(root, text="clear", padx=40, pady=20, command= button_clear,bd="5",bg="gray")

#put the buttons on the screen
but_1.grid(row=3, column=0)
but_2.grid(row=3, column=1)
but_3.grid(row=3, column=2)

but_4.grid(row=1, column=0)
but_5.grid(row=1, column=1)
but_6.grid(row=1, column=2)

but_7.grid(row=2, column=0)
but_8.grid(row=2, column=1)
but_9.grid(row=2, column=2)

but_0.grid(row=4, column=1)

but_plus.grid(row=4, column=0)
but_equa.grid(row=5, column=2)
# button_clea.grid(row=5, column=2)

but_min.grid(row=4, column=2)
but_mut.grid(row=5, column=1)
but_div.grid(row=5, column=0)


root.mainloop()
