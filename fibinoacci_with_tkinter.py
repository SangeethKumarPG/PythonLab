import tkinter as tk

def fibinoacci_in_limit(l,u):
    in_limit=[]
    fib=[]
    lower =l
    upper = u
    lower_value , upper_value=lower,upper

    if upper_value < lower_value:
        print("Please enter a valid limit")
    else:
        first_value,second_value = 0,1
        print("Fibinoacci sequence")
        fib=[0,1]
        Next=0
        while Next < upper_value:
            Next = first_value + second_value
            fib.append(Next)
            if Next in range(lower_value,upper_value):
                in_limit.append(Next)

            first_value=second_value
            second_value = Next
        lbl_fib.config(text=fib)
        lbl_fib_lm.config(text=in_limit)

def fibinoacci():
    lower = int(entryLower.get())
    upper = int(entryUpper.get())
    fibinoacci_in_limit(lower,upper)


window=tk.Tk()
window.title("fibinoacci in limit")
window.geometry("600x400")
window.resizable(0,0)

lbl_1 = tk.Label(text="lower::")
lbl_1.place(x=0,y=0,width=150,height = 25)

entryLower = tk.Entry(bg='white',fg='black')
entryLower.place(x=50, y=25,width=100,height=25)

lbl_2= tk.Label(text="Upper::")
lbl_2.place(x=175,y=0,width=100,height=25)

entryUpper = tk.Entry(bg='white',fg='black')
entryUpper.place(x=175,y=25,width=100,height=25)

btn=tk.Button(text='Calculate',command=fibinoacci)
btn.place(x=50,y=75,width=100,height=25)

lbl_3=tk.Label(text="Fib ::")
lbl_3.place(x=0,y=150,width=150,height=25)

lbl_fib = tk.Label(text="")
lbl_fib.place(x=100,y=150,width=250,height=25)

lbl_4=tk.Label(text="fib_in_limit::")
lbl_4.place(x=0,y=275,width=150,height=25)

lbl_fib_lm=tk.Label(text="")
lbl_fib_lm.place(x=150,y=275,width=250,height=25)

window.mainloop()