from tkinter import *

# window
window = Tk()
window.title("Tkinter Python")
window.minsize(600, 600)
window.config(padx=20, pady=20)

# label
my_label = Label(text ="my label")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.config(padx=10, pady=10)
my_label.pack()

def button_clicked():
    print("button clicked")
    print(my_text.get(1.0, END)) # 1 ->line -> satırı belirtiyor, 0 -> karakteri gösteriyor
# END -> son karaktere kadar işleme alınacağını gösteriyor.
# Text'e yazılanların kaçıncı satır ve kaçıncı karakterden işleme alınacağını gösteriyor.

# button
my_button = Button(text="Button", command= button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

# entry - single line
my_entry = Entry(width=20)
my_entry.focus() # program çalıştığında mouse'un nerede olacağını belirtmeye yarıyor.
my_entry.pack()

# text - multi line
my_text = Text(width=20, height=5)
# my_text.focus()
my_text.pack()

# scale
def scale_seleceted(value):
    print(value)
my_scale = Scale(from_=0, to=15, command= scale_seleceted)
my_scale.pack()

# spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0, to=20, command=spinbox_selected)
my_spinbox.pack()

# check_button
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar()
my_checkbutton = Checkbutton(text="Check", variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()

# radio_button

def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
my_radiobutton = Radiobutton(text="1. Opsiyon", value=10, variable= radio_checked_state, command=radio_selected)
my_radiobutton2 = Radiobutton(text="2. Opsiyon", value=20, variable= radio_checked_state, command=radio_selected)
my_radiobutton.pack()
my_radiobutton2.pack()

# listbox

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["Atıl", "Ali", "Süleyman", "Hüsnü", "Şükrü", "Zeki"]
for i in range(len(name_list)):
    my_listbox.insert(i, name_list[i])
my_listbox.bind('<<ListboxSelect>>', listbox_selected) #'<<ListboxSelect>>' -> fonksiyonu listbox'a bağlamada
# kullanılır. Sabit bir ifadedir.
my_listbox.pack()

window.mainloop()