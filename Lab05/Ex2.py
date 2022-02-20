import tkinter as tk

def evaluate(event):
    myString = entry.get()
    results = ""

    if (myString == 'Square'):
        for i in range(15):
            for j in range(15):
                results = results + '  *'
            results = results + '\n'

    if (myString == 'Triangle'):
        for i in range(15):
            for j in range(i):
                results += "    "
            results += "  0"
            for j in range(7 - i):
                results += "  *"
            for j in range(6 - i):
                results += "  *"
            if i < 7:
                results += "  0"
            for j in range(i):
                if i < 8:
                    results += "  *"
            for j in range(14 - i):
                if i > 7:
                    results += "  *"
            results += "\n"

    res.configure(text = "The output is: \n " + results)

w = tk.Tk()
tk.Label(w, text="Please Enter  format of the output (i.e. Square or Triangle):").pack()
entry = tk.Entry(w)
myString = entry.get()
print(myString)

entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()