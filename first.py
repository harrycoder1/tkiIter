import tkinter as tk 
from tkinter import messagebox
class GO :
    
    def close():
        print("hello")   
        if messagebox.askyesno(title="Quit ?" ,message="Do you want to Exit"):
            root.destroy() 
    def submit ():
        print(textbox.get('1.0' ,tk.END))
        # print( eval(str(textbox.get())))

root = tk.Tk()
root.geometry("500x500")
root.title("harish app")

label = tk.Label(root , text="Hello World" , font =('Arial' ,18))

label.pack(padx=20 , pady=20 )

# for text box 
textbox = tk.Text(root,height=2,font=("Arial" ,16) )
textbox.pack(padx=20 ,pady=20)

#one line input
myEntery = tk.Entry(root)
myEntery.pack()
ff = GO()
def submit ():
    #  print(eval())
    var =(eval(str(textbox.get('1.0' ,tk.END))))
    messagebox.showinfo(title="Calculation", message=var)
# buttons
button = tk.Button(root , text="Submit" , font=("Arial" ,18) , background="red" ,border=0 , command=submit)

button.pack(pady=30)
root.protocol("WM_DELETE_WINDOW" , GO.close)




root.mainloop()

