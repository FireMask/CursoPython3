import os
import helpers
import database as db

def init():
    while True:
        helpers.clear_screen()
        
        print("================")
        print("Welcome to Client Management")
        print("================")
        print("[1] List clients")
        print("[2] Search client")
        print("[3] New client")
        print("[4] Update client")
        print("[5] Delete client")
        print("[6] Exit")
        
        option = int(input("> "))
        helpers.clear_screen()
        
        match option:
            case 1:
                print("Listing all clients...")
                for client in db.Clients.list:
                    print(client)
                
            case 2:
                print("Searching client...")
                dni = helpers.read_text(3, 3, 'DNI (2 int and 1 char)').upper()
                client = db.Clients.search(dni)
                print(client) if client else print("Client not found")
                
            case 3:
                print("Adding new client...")
                
                dni = None
                while True:
                    dni = helpers.read_text(3, 3, 'DNI (2 int and 1 char)').upper()
                    if helpers.valid_dni(dni):
                        break
                    
                name = helpers.read_text(2, 30, 'Name (2-30 chars)').capitalize()
                lastname = helpers.read_text(2, 30, 'Lastname (2-30 chars)').capitalize()
                db.Clients.create(dni, name, lastname)
                print("Client added succesfully")
                
            case 4:
                print("Updating client...")
                dni = helpers.read_text(3, 3, 'DNI (2 int and 1 char)').upper()
                client = db.Clients.search(dni)
                if client is None:
                    print("Client not found")
                    pass
                
                name = helpers.read_text(2, 30, f'Name (2-30 chars) [{ client.name }]').capitalize()
                lastname = helpers.read_text(2, 30, f'Lastname (2-30 chars [{client.lastname }])').capitalize()
                db.Clients.update(client.dni, name, lastname)
                print("Client updated succesfully")
                
            case 5:
                print("Deleting client...")
                dni = helpers.read_text(3, 3, 'DNI (2 int and 1 char)').upper()
                print("Client removed succesfully") if db.Clients.delete(dni) else print("Client not found")
                
            case 6:
                print("Bye bye...")
                break
                
            case other:
                print("Option not found")
                
                
        input("\nPress ENTER to continue...")