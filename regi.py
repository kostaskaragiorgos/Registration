from tkinter import *
from tkinter import messagebox as msg
from tkinter import simpledialog as sd

import os

import datetime

import cv2

class Registration():
    def __init__(self,master):
        self.master = master
        self.master.title("Registration")
        self.master.geometry("250x200")
        self.master.resizable(False,False)
        this_year = datetime.datetime.now()
        if os.path.exists(str(this_year.year)) == False:
            os.mkdir(str(this_year.year))
        os.chdir(str(this_year.year))
        if os.path.exists(str(this_year.month)) == False:
            os.mkdir(str(this_year.month))
        os.chdir(str(this_year.month))
        self.flagloadname = 0
        self.amleb = Label(self.master,text = "Name")
        self.amleb.pack()
        
        self.textname = Text(self.master,height = 1 )
        self.textname.pack()
        
        self.surname = Label(self.master , text ="Surname")
        self.surname.pack()
        
        self.textsurname = Text(self.master,height = 1 )
        self.textsurname.pack()
        
        self.inmpfoto = Button(self.master,text= "Upload a foto",command = self.upload)
        self.inmpfoto.pack()
        
        self.add = Button(self.master,text= "Add",command = self.addp)
        self.add.pack()
        
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "New Event",accelerator = 'Alt+O',command = self.newevent)
        self.file_menu.add_command(label = "Load Event",accelerator = 'Alt+T', command = self.loadevent)
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
    
    def loadevent(self):
        event_load = sd.askstring("Load an event","Enter the name of the event",parent = self.master)
    
    def newevent(self):
        event_name = sd.askstring("Name of the event","Enter the name of the event",parent = self.master)
    
    def addp(self):
        if self.flagloadname == 0:
            msg.showerror("Error","Create an event or load one")
            
    def upload(self):
        if self.flagloadname == 0:
            msg.showerror("Error","Create an event or load one")
        else:
            camera = cv2.VideoCapture(0)
            while True:
                return_value , image = camera.read()
                cv2.imshow('image',image)
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    cv2.imwrite('image.jpg',image)
                    break
            camera.release()
            cv2.destroyAllWindows()
        
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