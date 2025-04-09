#Example: Create a dynamic platform to access information about various universities.

from tkinter import *
#def nur():
def nur1():
    label_box1.configure(text="Oksford Universiteti dünyanın ən qədim ingilisdilli universitetidir."
                              "Lakin o məlumdur ki, Oksfordda təhsilə 1096-cı ildə başlanılıb")
def nur2():
    label_box1.configure(text="Harvard Universiteti  — ABŞ-nin və dünyanın ən məşhur universitetlərindən biri."
                              "Əsası 1636-cı ilin 8 sentyabrında qoyulmuşdur.""Universitetin əsas kapitalı 34,9 milyard ABŞ dollarıdır.")
def nur3():
    label_box1.configure(text="Universitet 1209-cu ildə bir Oksford tələbəsinin qadını öldürməsindən sonra bir qrup alim şəhəri tərk etmiş və "
                              "Kembricdə universitet təsis etmişdir.1214-cü ildə universitet qaydaları tərtiv edilmişdir."
                              "Bu qaydalarda rektorun təyini və imtahanların verilmə qaydaları müəyyən edilmişdi. ")
def nur4():
    label_box1.configure(text="Stanford Universiteti— Palo-Alto şəhəri yaxınlığında, Silikon vadisinin mərkəzində, Kaliforniya ştatında yerləşir"
                              " Bu universiteti Silikon vadisinin sərvəti adlandırırlar. Universitet ABŞ-nin və bütün dünyanın ən nüfuzlu"
                              "ali təhsil müəssisələrindən biridir.")

root = Tk()

root.title("nur aplication")
root.geometry("600x300")
root.config(bg='#b0ffff')


buttonbox=Button(root, text = 'tun off',    bg='red', width=10, height=2, fg='yellow', relief=SUNKEN,bd=4 )
buttonbox.place(x=510, y=250)
buttonbox=Button(root, text = 'tun on',    bg='green', width=10, height=2, fg='yellow', relief=SUNKEN,bd=4 )
buttonbox.place(x=440, y=250)


button1 = Button(root, text="Oxford", bg="blue", fg="white", width=15, height=2, relief=RIDGE, bd=8, command = nur1)
button1.place(x=10, y=20)

button2 = Button(root, text="Harvard", bg="darkgrey", fg="black", width=15, height=2,relief=RIDGE, bd=8, command=nur2)
button2.place(x=10, y=70)

button3 = Button(root, text="Cambridge", bg="yellow", fg="black", width=15, height=2, relief=RIDGE, bd=8, command=nur3)
button3.place(x=10, y=120)

button4 = Button(root, text="Stanford", bg="orange", fg="black", width=15, height=2, relief=RIDGE, bd=8,command=nur4)
button4.place(x=10, y=170)


label_box1 = Label(
    root,
    text="Universitetler haqqinda melumatlar",
    font=("Arial", 10, "bold"),    bg="green",    fg="black",    width=40,    height=10,  relief=RIDGE, bd=14,  anchor="center",    wraplength=300)
label_box1.place(x=150, y=20)
root.mainloop()