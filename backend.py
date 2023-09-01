import tkinter as tk 
from tkinter import messagebox
class MyGUI :
    def __init__(self) :
        self.root = tk.Tk()
        
        self.menubar =tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar , tearoff=0)
        self.filemenu.add_command(label="Close" , command=self.on_closing)
        
        self.menubar.add_cascade(menu=self.filemenu , label="file")
        self.root.config(menu=self.menubar)
        
        self.label = tk.Label(self.root , text="Your Message" ,  font=("Arial" ,18))
        self.label.pack(padx=10 , pady=10)
        
        self.texbox = tk.Text(self.root ,height=5, font=("Arial" ,16))
        self.texbox.pack(padx=10 ,pady=10)
        self.texbox.bind("<KeyPress>" , self.shortcut)
        self.check_stat = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root ,text="Show msg box" ,font=("Arial" ,16), variable=self.check_stat)
        self.check.pack(padx=10 ,pady=10)
        
        
        self.button = tk.Button(self.root ,text="Show message" ,font=("Arial" ,18),command=self.showmessage )
        self.button.pack(padx=10 ,pady=10)
        self.root.protocol("WM_DELETE_WINDOW" ,self.on_closing)
        
        self.root.mainloop()
        
    def showmessage(self):
        print(self.check_stat.get())
        if self.check_stat.get() ==0 :
            print(self.texbox.get('1.0' ,tk.END))
            messagebox.showwarning(title="Warning" ,message="Please clike on checkbox")
        else :
            messagebox.showinfo(title="Message" ,message=self.texbox.get('1.0', tk.END))
    
    def shortcut(self , event) :
        print(event)
    
    def on_closing(self):
        print("HEllo world")
        if messagebox.askyesno(title="Quit?",message="Do you realy want to QUit from app "):
            self.root.destroy()
    
            
        
c = MyGUI()
 