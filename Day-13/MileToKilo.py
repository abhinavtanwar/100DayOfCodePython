from tkinter import *

def MTK():
    print("I got clicked")
    new_text = round(int(input_field.get()) * 1.6, 2)
    my_label2.config(text=new_text)


window = Tk()
window.minsize(width=200, height=100)
window.title("Mile to Kilometer Converter")
window.config(padx=10, pady=10)

# label
my_label = Label(text="miles")
my_label.grid(column=2, row=0)

my_label1 = Label(text="is equal to")
my_label1.grid(column=0, row=1)

my_label2 = Label(text="")
my_label2.grid(column=1, row=1)

my_label3 = Label(text="Kilometers")
my_label3.grid(column=2, row=1)

# Entry
input_field = Entry(width=10)
print(input_field.get())
input_field.grid(column=1, row=0)

# button
button = Button(text="Click to Convert", command=MTK)
# button.config(width=5, height=1)
button.grid(column=1, row=2)

window.mainloop()
