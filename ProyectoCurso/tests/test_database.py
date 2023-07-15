import helpers
import csv
import config
import copy
import unittest
import database as db

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        db.Clients.list = [
            db.Client('31A', 'Andres', 'Lira'),
            db.Client('27J', 'Joice', 'Lopez'),
            db.Client('03C', 'Canela', 'Dog'),
            db.Client('02L', 'Lola', 'Dog')
        ]
        
    def test_search_client(self):
        exisiting_client = db.Clients.search('31A')
        nonexisiting_client = db.Clients.search('00X')
        self.assertIsNotNone(exisiting_client)
        self.assertIsNone(nonexisiting_client)
        
    def test_create_client(self):
        new_client = db.Clients.create('00A', 'Test1', 'Test2')
        self.assertEqual(len(db.Clients.list), 5)
        self.assertEqual(new_client.dni, '00A')
        self.assertEqual(new_client.name, 'Test1')
        self.assertEqual(new_client.lastname, 'Test2')
        
    def test_update_client(self):
        client_to_modify = copy.copy(db.Clients.search('03C'))
        modified_client = db.Clients.update('03C', 'Isabelle', 'Dog')
        self.assertEqual(client_to_modify.name, 'Canela')
        self.assertEqual(modified_client.name, 'Isabelle')
        
    def test_delete_client(self):
        deleted_client = db.Clients.delete('31A')
        searched_client = db.Clients.search('31A')
        self.assertEqual(deleted_client.dni, '31A')
        self.assertIsNone(searched_client)
        
    def test_valid_dni(self):
        self.assertTrue(helpers.valid_dni('00A'))
        self.assertFalse(helpers.valid_dni('232323S'))
        self.assertFalse(helpers.valid_dni('00a'))
        self.assertFalse(helpers.valid_dni('F00'))
        
    def test_write_csv(self):
        db.Clients.delete('31A')
        db.Clients.delete('27J')
        db.Clients.update('03C', 'Canelita', 'Dog')
        
        dni, name, lastname = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as file:
            reader = csv.reader(file, delimiter=',')
            dni, name, lastname = next(reader)
        
        self.assertEqual(dni, '03C')
        self.assertEqual(name, 'Canelita')
        self.assertEqual(lastname, 'Dog')