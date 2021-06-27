import tkinter as t
app = t.Tk()
app.title("Basic Arithmatic")
app.geometry('300x200')
result = t.Variable(app)
result.set('Result')
t.Label(app, textvariable=result).place(x=140, y=140)
first_val = t.Variable(app)
second_val = t.Variable(app)
t.Entry(app, textvariable=first_val, width=10).place(x=50, y=20)
t.Entry(app, textvariable=second_val, width=10).place(x=160, y=20)


def operate(e):
    first = first_val.get()
    second = second_val.get()
    exp = first + e + second
    result.set(eval(exp))


t.Button(app, text='+', command=lambda: operate('+')).place(x=50, y=70)
t.Button(app, text='-', command=lambda: operate('-')).place(x=100, y=70)
t.Button(app, text='x', command=lambda: operate('*')).place(x=160, y=70)
t.Button(app, text='/', command=lambda: operate('/')).place(x=210, y=70)
app.mainloop()