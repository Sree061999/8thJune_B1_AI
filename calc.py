import tkinter as t
app = t.Tk()
app.title('Calculator')
app.geometry('400x300')
app.configure(bg='grey')
clear = t.Variable(app)
result = t.Variable(app)
t.Label(app, textvariable=result, width='50', height='3', bg='white').place(x=40, y=20)
exp = ''


def operate(e):
    global exp
    if e == "":
        exp = ""
        result.set(exp)
    elif e == '=':
        tot = str(eval(exp))
        result.set(tot)
    else:
        exp += e
        result.set(exp)


t.Button(app, text='clr', command=lambda: operate("")).place(x=5, y=2)
t.Button(app, text='7', width='3', command=lambda: operate('7')).place(x=60, y=100)
t.Button(app, text='8', width='3', command=lambda: operate('8')).place(x=160, y=100)
t.Button(app, text='9', width='3', command=lambda: operate('9')).place(x=260, y=100)
t.Button(app, text='+', width='3', command=lambda: operate('+')).place(x=360, y=100)
t.Button(app, text='4', width='3', command=lambda: operate('4')).place(x=60, y=150)
t.Button(app, text='5', width='3', command=lambda: operate('5')).place(x=160, y=150)
t.Button(app, text='6', width='3', command=lambda: operate('6')).place(x=260, y=150)
t.Button(app, text='-', width='3', command=lambda: operate('-')).place(x=360, y=150)
t.Button(app, text='1', width='3', command=lambda: operate('1')).place(x=60, y=200)
t.Button(app, text='2', width='3', command=lambda: operate('2')).place(x=160, y=200)
t.Button(app, text='3', width='3', command=lambda: operate('3')).place(x=260, y=200)
t.Button(app, text='x', width='3', command=lambda: operate('*')).place(x=360, y=200)
t.Button(app, text='.', width='3', command=lambda: operate('.')).place(x=60, y=250)
t.Button(app, text='0', width='3', command=lambda: operate('0')).place(x=160, y=250)
t.Button(app, text='=', width='3', command=lambda: operate('=')).place(x=260, y=250)
t.Button(app, text='/', width='3', command=lambda: operate('/')).place(x=360, y=250)
app.mainloop()