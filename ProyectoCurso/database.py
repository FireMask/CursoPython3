import csv
import config

class Client:
    def __init__(self, dni, name, lastname):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        
    def __str__(self):
        return f'({self.dni}) - {self.name} {self.lastname}'
    
class Clients:
    list = []
    
    with open(config.DATABASE_PATH, newline='\n') as file:
        reader = csv.reader(file, delimiter=',')
        for dni, name, lastname in reader:
            client = Client(dni, name, lastname)
            list.append(client)
    
    @staticmethod
    def search(dni):
        for client in Clients.list:
            if client.dni == dni:
                return client
        return None
            
    @staticmethod
    def create(dni, name, lastname):
        if Clients.search(dni) is not None:
            print("Client DNI already exist in database")
            return None
        
        client = Client(dni, name, lastname)
        Clients.list.append(client)
        Clients.save()
        return client
    
    @staticmethod
    def update(dni, name, lastname):
        client = Clients.search(dni)
        if client is not None:
            client.name = name
            client.lastname = lastname
            Clients.save()
            return client
        
    @staticmethod
    def delete(dni):
        for idx, client in enumerate(Clients.list):
            if client.dni == dni:
                deleted_client = Clients.list.pop(idx)
                Clients.save()
                return deleted_client
            
    @staticmethod
    def save():
        with open(config.DATABASE_PATH, 'w', newline='\n') as file:
            writer = csv.writer(file, delimiter=',')
            for client in Clients.list:
                writer.writerow((client.dni, client.name, client.lastname))
            
    