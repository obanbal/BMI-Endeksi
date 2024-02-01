import tkinter

window = tkinter.Tk()
window.title("BMI Calculator - Vücut Kitle İndeksi")
window.minsize(600,400)
window.config(padx=20, pady=20)


my_label = tkinter.Label(text="Enter Your Weight - Kilonuzu Giriniz (Kg) :", font=('Times', 15, 'normal'))
my_label.config(bg="light blue", fg="black")
my_label.pack()
my_label.config(padx=10, pady=10)

my_entry = tkinter.Entry(width=30)
my_entry.config(bg="light blue")
my_entry.pack()


my_label2 = tkinter.Label(text="Enter Your Height - Boyunuzu Giriniz (Cm) :", font=('Times', 15, 'normal'))
my_label2.config(bg="light blue", fg="black")
my_label2.pack()
my_label2.config(padx=10, pady=10)

my_entry2 = tkinter.Entry(width=30)
my_entry2.config(bg="light blue")
my_entry2.pack()

def button_calculate():
    try:
        agirlik= (int(my_entry2.get())/100)**2
        bmi=(int(my_entry.get())/agirlik)
        if bmi<18.5:
            my_label3 = tkinter.Label(text= f"Vücut Kitle İndeksiniz : {bmi}. Bu orana göre siz düşük kilolusunuz",
                                      font=('Times', 15, 'normal'))
            my_label3.grid_bbox(row=6, column=0)
        elif bmi>18.5 and bmi<24.9:
            my_label3 = tkinter.Label(text=f"Vücut Kitle İndeksiniz : {bmi}. Bu orana göre siz normal kilolusunuz",
                                      font=('Times', 15, 'normal'))
            my_label3.grid_bbox(row=6, column=0)
        elif bmi>25.0 and bmi<29.9:
            my_label3 = tkinter.Label(text=f"Vücut Kitle İndeksiniz : {bmi}. Bu orana göre siz kilolusunuz",
                                      font=('Times', 15, 'normal'))
            my_label3.grid_bbox(row=6, column=0)
        elif bmi>30.0 and bmi<40.0:
            my_label3 = tkinter.Label(text=f"Vücut Kitle İndeksiniz : {bmi}. Bu orana göre siz obezsiniz",
                                      font=('Times', 15, 'normal'))
            my_label3.grid_bbox(row=6, column=0)
        elif bmi>40.0:
            my_label3 = tkinter.Label(text=f"Vücut Kitle İndeksiniz : {bmi}. Bu orana göre siz aşırı obezsiniz",
                                      font=('Times', 15, 'normal'))
            my_label3.grid_bbox(row=6, column=0)
        my_label3.config(bg="light blue", fg="black")
        my_label3.pack()
        my_label3.grid_bbox(row=6, column=0)
    except:
        my_label3 = tkinter.Label(text="Lütfen Sayısal Veri Giriniz", font=('Times', 15, 'normal'))
        my_label3.grid_bbox(row=6, column=0)
        my_label3.config(bg="light blue", fg="black")
        my_label3.pack()

my_button = tkinter.Button(text="Calculate - Hesapla", font=('Times', 15, 'normal'), command=button_calculate)
my_button.pack()

window.mainloop()