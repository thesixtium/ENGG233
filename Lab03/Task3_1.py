import tkinter as tk

def evaluate(event):
    myString=entry.get()
    results = myString[::-1]
    res.configure(text="The Reverse String is:"+results)

w = tk.Tk()
tk.Label(w, text="Please Enter a string with 4 characters (e.g.ABCD): ").pack()
entry = tk.Entry(w)
myString = entry.get()
print(myString)
entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()
