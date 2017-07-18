from Tkinter import *

def addition_function():
    firstnumber=firstItemVar.get()
    secondnumber=secondItemVar.get()
    addresult=int(firstnumber)+int(secondnumber)
    resVar.set(addresult)
    return addresult
def minus_function():
    firstnumber=firstItemVar.get()
    secondnumber=secondItemVar.get()
    minus=int(firstnumber)-int(secondnumber)
    resVar.set(minus)
    return minus
def divide_function():
    firstnumber = firstItemVar.get()
    secondnumber = secondItemVar.get()
    divide = int(firstnumber)/int(secondnumber)
    resVar.set(divide)
    return divide
def multiply_function():
    firstnumber = firstItemVar.get()
    secondnumber = secondItemVar.get()
    multiply = int(firstnumber)*int(secondnumber)
    resVar.set(multiply)
    return multiply
def restart_function():
    firstItemVar.set('0')
    secondItemVar.set('0')
    resVar.set("")
    return
def number7_function():
    showVar.set(7)
    shownumber=showVar
    if shownumber!="":

    return

def number8_function():
    shownumber=showVar.get()
    if shownumber!="":
        shownumber+=showVar.get()
    return shownumber
def number9_function():
    shownumber=showVar.get()
    if shownumber!="":
        shownumber+=showVar.get()
    return shownumber

root = Tk()
root.title('Calculator')
resVar = StringVar()
resEntry = Entry(textvariable=resVar, width=40, state='disabled')
resEntry.grid(row=0, column=0, columnspan=2)
showVar=StringVar()
showEntry=Entry(textvariable=showVar,width=40,state='disabled')
showEntry.grid(row=1,column=0,columnspan=2)
firstItemLabel = Label(text='First item:', width=10)
firstItemLabel.grid(row=2, column=0)
firstItemVar = StringVar()
firstItemVar.set('10')
firstItemEntry = Entry(textvariable=firstItemVar, width=10)
firstItemEntry.grid(row=2,column=1)
secondItemLabel = Label(text='Second item:', width=10)
secondItemLabel.grid(row=3, column=0)
secondItemVar = StringVar()
secondItemVar.set(2)
secondItemEntry = Entry(textvariable=secondItemVar, width=10)
secondItemEntry.grid(row=3,column=1)

number7_button=Button(text='7',command=number7_function,width=10)
number7_button.grid(row=4,column=0)
number8_button=Button(text='8',command=number8_function,width=10)
number8_button.grid(row=4,column=1)
number9_button=Button(text='9',command=number9_function,width=10)
number9_button.grid(row=4,column=2)

restart_button=Button(text='C',command=restart_function,width=10)
restart_button.grid(row=4,column=3)
divide_button=Button(text='/',command=divide_function,width=10)
divide_button.grid(row=5,column=3)
multiply_button=Button(text='*',command=multiply_function,width=10)
multiply_button.grid(row=6,column=3)
minus_button=Button(text='-',command=minus_function,width=10)
minus_button.grid(row=7,column=3)
addition_button=Button(text='+',command=addition_function,width=10)
addition_button.grid(row=8,column=3)





root.mainloop()



