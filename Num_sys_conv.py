import tkinter as tk
root=tk.Tk()

root.title("Number system converter")
root.geometry('300x200-50+50')

inactive_color='light pink'
active_color='light green'

dec_val=00000000
bin_val=0b00000000
hex_val=0x00000000

def dec_activate(event):
    decimal.configure(background=active_color)
    binary.configure(background=inactive_color)
    hexa.configure(background=inactive_color)

def bin_activate(event):
    decimal.configure(background=inactive_color)
    binary.configure(background=active_color)
    hexa.configure(background=inactive_color)
def hex_activate(event):
    decimal.configure(background=inactive_color)
    binary.configure(background=inactive_color)
    hexa.configure(background=active_color)

def take_dec_val(event):
    entry_box.configure(state=tk.NORMAL)

def displaydec(event):
    decimal_val=entry_box.get()
    binary_val=bin(int(decimal_val))
    hexa_val=hex(int(decimal_val))
    dec_label.configure(text=decimal_val)
    bin_label.configure(text=binary_val[2:])
    hex_label.configure(text=hexa_val[2:].upper())


Num_Buttons=tk.Frame(root,borderwidth=10)
display=tk.Frame(root)
entry=tk.Frame(root)

decimal=tk.Button(Num_Buttons,text="DEC",background='grey',height=2,width=10,border=4)
dec_label=tk.Label(display,text=dec_val,background='pink',height=2,width=20,border=4,borderwidth=5,relief='groove')
binary=tk.Button(Num_Buttons,text="BIN",background='grey',height=2,width=10,border=4)
bin_label=tk.Label(display,text=bin_val,background='pink',height=2,width=20,border=4,borderwidth=5,relief='groove')
hexa=tk.Button(Num_Buttons,text="HEX",background='grey',height=2,width=10,border=4)
hex_label=tk.Label(display,text=hex_val,background='pink',height=2,width=20,border=4,borderwidth=5,relief='groove')

text=tk.StringVar()
entry_box=tk.Entry(entry,textvariable=text,bd=5,border=5,cursor='right_side',relief='groove',width=15,state=tk.DISABLED)
entry_box.grid(row=0,column=0)

entry_box.bind('<Return>',displaydec)

decimal.grid(row=0,column=0)
dec_label.grid(row=0,column=0)
binary.grid(row=1,column=0)
bin_label.grid(row=1,column=0)
hexa.grid(row=2,column=0)
hex_label.grid(row=2,column=0)

decimal.bind('<Button>',dec_activate)
decimal.bind('<Button>',take_dec_val,add='+')
binary.bind('<Button>',bin_activate)
hexa.bind('<Button>',hex_activate)

Num_Buttons.grid(row=0,column=0)      
display.grid(row=0,column=1)
entry.grid(row=1,column=0)


root.mainloop()