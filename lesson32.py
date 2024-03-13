# Сервис доставки продуктов
import psycopg2
from psycopg2 import OperationalError

def connect_to_db():
    try:
        connect = psycopg2.connect(host = '127.0.0.1', 
                                port = 5432, 
                                dbname = 'postgres', 
                                user = 'postgres', 
                                password = 'postgres')
        return connect
    except OperationalError as error:
        print(f'The error{error}occured')

connection = connect_to_db()
cursor = connection.cursor()


class Order:
    def __init__(self, id, name, description, price, availability):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability
    

class Check(Order):
    def check(self):
        check = f"select * from delivery"
        print(check)
   
        
class Add(Order):
    def add(self):
        add = f"insert into delivery values(1, 'Milk', 'A milk', 800, 'Available')"
        cursor.execute(add)
        connection.commit()
     
        
class Delete(Order):
    def delete(self):
        delete = f"delete from delivery where id = 1"
        cursor.execute(delete)
        connection.commit()
        

class Update(Order):
    def update(self):
        update = f"update delivery set name = 'Apple' where id = 2"
        cursor.execute(update)
        connection.commit()    
        
while True:
    print('Choose an action')
    choice = input('1. Check\n2. Add\n3. Update\n4. Delete\n5. Exit\n\n')
    match choice:
        case '1':
            