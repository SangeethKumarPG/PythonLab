import tkinter as tk

def count():
    text = TextArea.get("1.0","end")
    prev = ' '
    count = 0
    for x in text:
        if prev == ' ' and x!=' ' and x!= "\n":
            count+=1
        prev = x
    lbl_count.config(text=count)

window = tk.Tk()
window.title("Factorial")
window.geometry("600x600")
window.resizable(0,0)

TextArea = tk.Text(bg='white', fg='black')
TextArea.place(x=50,y=25,width=500,height=200)

btn = tk.Button(text='Calculate', command=count)
btn.place(x=50,y=250,width=100, height=25)

lbl = tk.Label(text="Word count::",relief=tk.FLAT)
lbl.place(x=0,y=300,width=150,height=25)

lbl_count = tk.Label(text="", relief=tk.FLAT)
lbl_count.place(x=120,y=300,width=250,height=25)

window.mainloop()
