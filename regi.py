""" conf registration main file """
from tkinter import Menu, Text, Label, END, DISABLED, NORMAL, Tk, Button
from tkinter import messagebox as msg
from tkinter import simpledialog as sd
import os
import csv
import datetime
import cv2
import pandas as pd
def guestsfilecreation():
    """ creates a guests csv file """
    with open('guests.csv', 'a+') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Name', 'Surname', 'Available photo'])
def savetoevents(event_name):
    """ creates an events csv file """
    with open('events.csv', 'a+') as f:
        thewriter = csv.writer(f)
        thewriter.writerow([event_name])
def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "Create or Load an event add your name and surname and if you want a foto of you and press add button ")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Registration\nVersion 1.0")
def foldercreation(filename):
    """ creates a directory and sets it the current """
    if not os.path.exists(filename):
        os.mkdir(filename)
    os.chdir(filename)

class Registration():
    """ registration class """
    def __init__(self, master):
        self.master = master
        self.master.title("Registration")
        self.master.geometry("250x200")
        self.master.resizable(False, False)
        self.avphoto = 'NO'
        # folders of the year and month
        self.this_year = datetime.datetime.now()
        foldercreation(str(self.this_year.year))
        foldercreation(str(self.this_year.month))
        # creation
        #file of the events of the month
        if not os.path.exists("events.csv"):
            with open('events.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['Name of the event'])
        self.flagloadname = 0
        self.amleb = Label(self.master, text="Name")
        self.amleb.pack()
        self.textname = Text(self.master, height=1)
        self.textname.pack()
        self.surname = Label(self.master, text="Surname")
        self.surname.pack()
        self.textsurname = Text(self.master, height=1)
        self.textsurname.pack()
        self.clearnamebutton = Button(self.master, text="Clear Name", command=self.cnamef)
        self.clearnamebutton.pack()
        self.clersurnamebutton = Button(self.master, text="Clear Surname", command=self.snamef)
        self.clersurnamebutton.pack()
        self.add = Button(self.master, text="Add", command=self.addp)
        self.add.pack()
        #menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="New Event", command=self.newevent)
        self.file_menu.add_command(label="Load Event", command=self.loadevent)
        self.file_menu.add_command(label="Close Event", command=self.close_event, state=DISABLED)
        self.file_menu.add_command(label="Add Member", accelerator='Alt+T', command=self.addp)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Clear Name", accelerator='Ctrl+N', command=self.cnamef)
        self.edit_menu.add_command(label="Clear Surname", accelerator='Ctrl+S', command=self.snamef)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show members", accelerator='Ctrl+T', command=self.show_members)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-t>', lambda event: self.addp())
        self.master.bind('<Control-n>', lambda event: self.cnamef())
        self.master.bind('<Control-s>', lambda event: self.snamef())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Control-t>', lambda event: self.show_members())
    def show_members(self):
        """ shows the members """
        if self.flagloadname == 0:
            msg.showerror("Error", "Create an event or load one")
        else:
            df = pd.read_csv("guests.csv")
            df.replace(r'\r\n', '', regex=True, inplace=True)
            msg.showinfo("Members", str(df))
    def close_event(self):
        """ closes the event"""
        os.chdir("..")
        self.flagloadname = 0
        msg.showinfo("SUCCESS", "EVENT SUCCESSFULLY CLOSED")
        self.file_menu.entryconfig(0, state=NORMAL)
        self.file_menu.entryconfig(1, state=NORMAL)
        self.file_menu.entryconfig(2, state=DISABLED)
    def cnamef(self):
        """ clears name text field"""
        self.textname.delete(1.0, END)
    def snamef(self):
        """ clears surname text field"""
        self.textsurname.delete(1.0, END)
    def loadeventuserinput(self):
        """ load event menu user input"""
        event_load = sd.askstring("Load an event", "Enter the name of the event", parent=self.master)
        while event_load is None or (not event_load.strip()):
            event_load = sd.askstring("Load an event", "Enter the name of the event", parent=self.master)
        return event_load
    def b_m_state_change(self):
        self.flagloadname += 1
        self.file_menu.entryconfig(0, state=DISABLED)
        self.file_menu.entryconfig(1, state=DISABLED)
        self.file_menu.entryconfig(2, state=NORMAL)
    def loadevent(self):
        """ loads an event """
        file = open("events.csv")
        if len(file.readlines()) < 2:
            msg.showerror("Error", "No events to load")
        else:
            event_load = self.loadeventuserinput()
            if str(event_load) in os.listdir():
                os.chdir(event_load)
                self.b_m_state_change()
                msg.showinfo("SUCCESS", "EVENT SUCCESSFULLY LOADED")
            else:
                msg.showerror("Error", "There is no such event try again")
        file.close()
    def neweventuserinput(self):
        """ User enters the name of the new event"""
        event_name = sd.askstring("Name of the event", "Enter the name of the event", parent=self.master)
        while event_name is None or (not event_name.strip()):
            event_name = sd.askstring("Name of the event", "Enter the name of the event", parent=self.master)
        return event_name

    def newevent(self):
        """ new event """
        event_name = self.neweventuserinput()
        savetoevents(event_name)
        foldercreation(event_name)
        #file of the guests
        if not os.path.exists("guests.csv"):
            guestsfilecreation()
            self.b_m_state_change()
            msg.showinfo("SUCCESS", "EVENT SUCCESSFULLY CREATED")
        else:
            msg.showerror("Error", "This event already exists")
    def takepicture(self):
        """ takes a picture of a guest """
        camera = cv2.VideoCapture(0)
        while True:
            check, image = camera.read()
            cv2.imshow('image', image)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite(str(self.textname.get(1.0, END))+str(self.textsurname.get(1.0, END))+'.jpg', image)
                break
            camera.release()
            cv2.destroyAllWindows()
    
    def save_guests(self):
        """ saves the name and the surname of a guest """
        with open('guests.csv', 'a+') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([str(self.textname.get(1.0, END)), str(self.textsurname.get(1.0, END)), self.avphoto])
        msg.showinfo("INFO", "Name:"+str(self.textname.get(1.0, END))+"Surname:"+str(self.textsurname.get(1.0, END)))

    def addp(self):
        """ adds an event member""" 
        if self.flagloadname == 0:
            msg.showerror("Error", "Create an event or load one")
        else:
            if self.textname.count(1.0, END) == (1, ):
                msg.showerror("Error", "You have to add  name")
            else:
                self.save_guests()
                if msg.askokcancel('Take picture', 'Do you want to take a picture'):
                    self.takepicture()
                    self.avphoto = 'YES'
            self.snamef()
            self.cnamef()
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """
    root = Tk()
    Registration(root)
    root.mainloop()
if __name__ == '__main__':
    main()
