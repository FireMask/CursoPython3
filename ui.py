import helpers
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING

class CenterWidgetMixin:
    def center(self):
        self.update()
        #Width x Height + OffsetX + OffsetY
        # self.geometry("500x500+500+500")
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")

class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
      super().__init__(parent)
      self.title("New client")
      self.build()
      self.center()
      self.transient(parent)
      self.grab_set()
      
    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)
        
        Label(frame, text="DNI (2 ints y 1 char)").grid(row=0, column=0)
        Label(frame, text="Name (2-30 char)").grid(row=0, column=1)
        Label(frame, text="Lastname (2-30 char)").grid(row=0, column=2)
        
        dni_entry = Entry(frame)
        dni_entry.grid(row=1, column=0)
        dni_entry.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        
        name_entry = Entry(frame)
        name_entry.grid(row=1, column=1)
        name_entry.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        
        lastname_entry = Entry(frame)
        lastname_entry.grid(row=1, column=2)
        lastname_entry.bind("<KeyRelease>", lambda event: self.validate(event, 2))
        
        frame = Frame(self)
        frame.pack(pady=10)
        
        create = Button(frame, text="New", command=self.create_client)
        create.configure(state=DISABLED)
        create.grid(row=0, column=0)
        
        Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)
        
        self.validations = [0, 0, 0]
        self.create = create
        self.dni_entry = dni_entry
        self.name_entry = name_entry
        self.lastname_entry = lastname_entry
        
    def create_client(self):
        self.master.treeview.insert(
            parent='',
            index='end', #agregar al final
            iid= self.dni_entry.get(), #uuid
            values=(
                self.dni_entry.get(), 
                self.name_entry.get(), 
                self.lastname_entry.get()
            )
        )
        db.Clients.create(
            self.dni_entry.get(), 
            self.name_entry.get(), 
            self.lastname_entry.get()
        )
        self.close()
    
    def close(self):
        self.destroy()
        self.update()
        
    def validate(self, event, index):
        value = event.widget.get()
        match index:
            case 0:
                valid = helpers.valid_dni(value) and db.Clients.search(value) is None
            case 1:
                valid = value.isalpha() and (2 <= len(value) <= 30)
            case 2:
                valid = value.isalpha() and (2 <= len(value) <= 30)
            case other:
                valid = False
                
        event.widget.configure({"bg": f"{'Green' if valid else 'Red'}"})
        #Update button status
        self.validations[index] = valid
        self.create.config(state=NORMAL if self.validations == [1, 1, 1] else DISABLED)

class EditClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
      super().__init__(parent)
      self.title("Edit client")
      self.build()
      self.center()
      self.transient(parent)
      self.grab_set()
      
    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)
        
        Label(frame, text="DNI (No editable)").grid(row=0, column=0)
        Label(frame, text="Name (2-30 char)").grid(row=0, column=1)
        Label(frame, text="Lastname (2-30 char)").grid(row=0, column=2)
        
        dni_entry = Entry(frame)
        dni_entry.grid(row=1, column=0)
        
        name_entry = Entry(frame)
        name_entry.grid(row=1, column=1)
        name_entry.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        
        lastname_entry = Entry(frame)
        lastname_entry.grid(row=1, column=2)
        lastname_entry.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        
        client = self.master.treeview.focus()
        fields = self.master.treeview.item(client, 'values')
        dni_entry.insert(0, fields[0])
        dni_entry.config(state=DISABLED)
        name_entry.insert(0, fields[1])
        lastname_entry.insert(0, fields[2])
        
        frame = Frame(self)
        frame.pack(pady=10)
        
        update_button = Button(frame, text="Update", command=self.update_client)
        update_button.grid(row=0, column=0)

        Button(frame, text="Cancel", command=self.close).grid(row=0, column=1)
        
        self.validations = [1, 1]
        self.update_button = update_button
        self.dni_entry = dni_entry
        self.name_entry = name_entry
        self.lastname_entry = lastname_entry
        
    def update_client(self):
        client = self.master.treeview.focus()
        self.master.treeview.item(client, values=(
            self.dni_entry.get(), 
            self.name_entry.get(), 
            self.lastname_entry.get()
        ))
        db.Clients.update(
            self.dni_entry.get(), 
            self.name_entry.get(), 
            self.lastname_entry.get()
        )
        self.close()
    
    def close(self):
        self.destroy()
        self.update()
        
    def validate(self, event, index):
        value = event.widget.get()
        match index:
            case 0:
                valid = value.isalpha() and (2 <= len(value) <= 30)
            case 1:
                valid = value.isalpha() and (2 <= len(value) <= 30)
            case other:
                valid = False
                
        event.widget.configure({"bg": f"{'Green' if valid else 'Red'}"})
        #Update button status
        self.validations[index] = valid
        self.update_button.config(state=NORMAL if self.validations == [1, 1] else DISABLED)

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title("Client Management")
        self.build()
        self.center()
        
    def build(self):
        frame = Frame(self)
        frame.pack()
        
        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('DNI', 'Name', 'Lastname')
        
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("DNI", anchor=CENTER)
        treeview.column("Name", anchor=CENTER)
        treeview.column("Lastname", anchor=CENTER)
        
        #Headers
        treeview.heading("DNI", text="DNI", anchor=CENTER)
        treeview.heading("Name", text="Name", anchor=CENTER)
        treeview.heading("Lastname", text="Lastname", anchor=CENTER)
        
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        treeview['yscrollcommand'] = scrollbar.set
        
        for client in db.Clients.list:
            treeview.insert(
                parent='',
                index='end', #agregar al final
                iid=client.dni, #uuid
                values=(client.dni, client.name, client.lastname)
            )
        
        treeview.pack()
        
        frame = Frame(self)
        frame.pack(pady=20)
        
        Button(frame, text="New", command=self.create).grid(row=0, column=0)
        Button(frame, text="Edit", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Delete", command=self.delete).grid(row=0, column=2)
        
        self.treeview = treeview
        
    def delete(self):
        client = self.treeview.focus()
        if client:
            fields = self.treeview.item(client, 'values')
            answer = askokcancel(
                title='Confirm',
                message=f"Delete {fields[1]} {fields[2]}?",
                icon=WARNING
            )
            if answer:
                self.treeview.delete(client)
                db.Clients.delete(fields[0])
                
    def create(self):
        CreateClientWindow(self)
        
    def edit(self):
        if self.treeview.focus():
            EditClientWindow(self)
        
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop() 