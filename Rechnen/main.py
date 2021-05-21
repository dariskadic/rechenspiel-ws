import os
import tkinter as tk

#print("Hi, das hier ist das Hauptmenue.")
#print("Hier kannst du entscheiden, welches der beiden Spiele du spielst.")
#print("Die Beiden Spiele sind ein Plusspiel und ein Minusspiel.")
#print("Wenn du das Plusspiel spielen willst, drück + und dann Enter.")
#print("Wenn du das Minusspiel spielen willst, drück - und dann Enter.")

root = tk.Tk()

label1 = tk.Label(text="Hi, das hier ist das Hauptmenue.")
label2 = tk.Label(text="Hier kannst du entscheiden, welches der beiden Spiele du spielst.")
label3 = tk.Label(text="Die beiden Spiele sind ein Plusspiel und ein Minusspiel.")

label1.config(font=('Arial', 35))
label2.config(font=('Arial', 35))
label3.config(font=('Arial', 35))



label1.pack()
label2.pack()
label3.pack()

canvas1 = tk.Canvas(root, width=300, height=350, bg='gray90', relief='raised')
canvas1.pack()

canvas2 = tk.Canvas(root, width=300, height=350, bg='gray90', relief='raised')
canvas2.pack()



def mcalc():
    os.system('python3 mcalc.py')

def pcalc():
    os.system('python3 pcalc.py')


button1 = tk.Button(text='      Plusspiel      ', command=pcalc, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=button1)

button2 = tk.Button(text='      Minusspiel      ', command=mcalc, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas2.create_window(150, 150, window=button2)

root.title("Rechenspiel")
root.mainloop()
