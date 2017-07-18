# 2014.8.10-2017.10.27
from Tkinter import *
def yearcount(yearstart, yearfinish):
    a = range(yearstart, yearfinish)
    x = 0
    for year in a:
        yeardays = 365
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            x += yeardays + 1
        else:
            x += yeardays
    return x

def monthcount(year,monthstart, monthfinish):
    a = range(monthstart, monthfinish)
    x = 0
    for month in a:
        monthdays = 30
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if month==2:
                x+=monthdays-1
            else:
                x+=monthdays-2
        else:
            if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                x += monthdays + 1
            else:
                x += monthdays
    return x

def countdate():
    start=start_var.get()
    end=end_var.get()
    yearstart,monthstart,daystart,yearfinsih,monthfinish,dayfinish=start_end_day(start,end)
    if yearstart == yearfinsih:
        if monthstart == monthfinish:
            datedays = int(dayfinish) - int(daystart)
            #print "1Days:", datedays
        else:
            datedays = monthcount(yearstart,monthfinish + 1, monthstart) - daystart + dayfinish
            #print "2Days:", datedays
    elif yearfinsih - yearstart == 1:
        datedays = monthcount(yearstart,int(monthstart), 13) + monthcount(yearfinsih,1, int(monthfinish)) - int(daystart) + int(dayfinish)
        #print datedays
    else:
        datedays = yearcount(int(yearstart) + 1, int(yearfinsih) - 1) + \
                   monthcount(yearstart,int(monthstart), 13) + monthcount(yearfinsih,1, int(monthfinish)) - \
                   int(daystart) + int(dayfinish)
        #print"3Days: ", datedays
    result_var.set(abs(datedays))
    return abs(datedays)

def start_end_day(datestart='20140810',datefinish='20171029'):
    yearstart, monthstart, daystart = int(datestart[:4]), int(datestart[4:6]), int(datestart[6:])
    yearfinsih, monthfinish, dayfinish = int(datefinish[:4]), int(datefinish[4:6]), int(datefinish[6:])
    print "Start from: ", yearstart, monthstart, daystart
    print "Finish to: ", yearfinsih, monthfinish, dayfinish
    return yearstart,monthstart,daystart,yearfinsih,monthfinish,dayfinish

#creat a window
lable_width=20
entry_width=20
button_width=lable_width+entry_width
root=Tk()
root.title('Count days!')#set the title of the pogram
#print welcome
info=Label(root,text="Welcome!",width=button_width)
info.grid(row=0,column=0,columnspan=2)
#print start form:
start_info=Label(root,text="Start form:",width=lable_width)
start_info.grid(row=1,column=0)
#set the type window for the start date

start_var=StringVar()
start_var.set('20140810')
start_Entry=Entry(root,width=entry_width,textvariable=start_var)
start_Entry.grid(row=1,column=1)
#print finish to:
end_info = Label(root, text="Finish to: ", width=lable_width)
end_info.grid(row=2, column=0)
#set the tpy window for the finish date
end_var = StringVar()
end_var.set('20171029')
end_Entry = Entry(root, width=entry_width, textvariable=end_var)
end_Entry.grid(row=2, column=1)
#set the button to calculate the dates
submit_button = Button(text='count days', command=countdate, width=button_width)
submit_button.grid(row=3, column=0, columnspan=2)
#print he dates
res_info = Label(root, text="Days:", width=lable_width)
res_info.grid(row=4, column=0)
#set the show window for the days
result_var = StringVar()
result_Entry = Entry(root, width=entry_width, textvariable=result_var, state='disabled')
result_Entry.grid(row=4, column=1)


root.mainloop()
