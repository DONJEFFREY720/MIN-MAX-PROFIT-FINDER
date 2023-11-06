# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 18:14:39 2023

@author: Don Jeffrey
"""

from tkinter import*
root=Tk()
root.title("PROFIT RECORD") 
root.geometry("600x400")
root.configure(bg="yellow")


months = ("JAN","FEB","MAR","API","MAY","JUNE","JULY","AUG","SEP","OCT","NOV","DEC")

months_label = Label(root,text="Months"+str(months))

profits = (500,1000,5000,10000,50000,100000,500000,1000000,5000000,10000000,5000,250000000)

profits_label = Label(root,text="Profits"+str(profits))

profit_max_label = Label(root,text="Maximum Profit:  ")

profit_min_label = Label(root,text="Minimum Profit:  ")


def Profit():

    profit_max = max(profits)

    Profit_index = profits.index(profit_max)
    
    Profit_month = months[Profit_index]
    
    print("The Maximum Profit Recorded is :"+str(profit_max)+"\n The Month Of Maximum Profit is :  "+str(Profit_month))

    profit_min = min(profits)
    
    Profit_index2 = profits.index(profit_min)
    
    Profit_month2 = months[Profit_index2]
    
    print("The Minimum Profit Recorded is :"+str(profit_min)+"\n The Month Of Minimum Profit is :  "+str(Profit_month2))

    profit_max_label["text"] = "Maximum Profit :   "+str(profit_max)+"  in  "+str(Profit_month)

    profit_min_label["text"] = "Minimum Profit :   "+str(profit_min)+"  in  "+str(Profit_month2)



Profit_gen = Button(root,text="Generate Profit",command=Profit,bg="blue",fg="white")
Profit_gen.place(relx=0.5,rely=0.6,anchor=CENTER)  
profits_label.place(relx=0.5,rely=0.2,anchor=CENTER)
months_label.place(relx=0.5,rely=0.1,anchor=CENTER)
profit_max_label.place(relx=0.5,rely=0.3,anchor=CENTER)
profit_min_label.place(relx=0.5,rely=0.4,anchor=CENTER)

root.mainloop()