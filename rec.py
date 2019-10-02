from tkinter import *
from tkinter import messagebox as msg

class Registration():
    def __init__(self,master):
        self.master = master
        self.master.title("Registration")
        self.master.geometry("250x200")
        self.master.resizable(False,False)
        
       
        
        self.amleb = Label(self.master,text = "Name")
        self.amleb.pack()
        
        self.textname = Text(self.master,height = 1 )
        self.textname.pack()
        
        self.surname = Label(self.master , text ="Surname")
        self.surname.pack()
        
        self.textsurname = Text(self.master,height = 1 )
        self.textsurname.pack()
        
        self.inmpfoto = Button(self.master,text= "Upload a foto")
        self.inmpfoto.pack()
    
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass

def main():
    root=Tk()
    R = Registration(root)
    root.mainloop()
    
if __name__=='__main__':
    main()