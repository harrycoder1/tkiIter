import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("harish app")

label = tk.Label(root, text="Hello World", font=('Arial', 18))
label.pack(padx=20, pady=20)

var = tk.StringVar()
textbox = tk.Text(root, height=2, font=("Arial", 16) )
textbox.pack(padx=20, pady=20)

buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
n=1

for i in range(0,3):
    for j in range(0,3):
        btn1 = tk.Button(buttonFrame, text=n, font=("Arial", 18))
        btn1.grid(row=i, column=j, sticky="ew")
        n=n+1
        



buttonFrame.pack(fill='x')

anotherBtn = tk.Button(root,text="Test")
anotherBtn.place(x=300 , y=330 ,height=100 , width=100)
root.mainloop()
