from abc import ABC, abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data):
        pass 
    @abstractmethod
    def update(self, record_id, data):
        pass 
    @abstractmethod
    def delete(self, record_id):
        pass 
class SQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting {data} into SQL database.")

    def update(self, record_id, data):
        print(f"Updating record {record_id} in SQL database with {data}.")

    def delete(self, record_id):
        print(f"Deleting record {record_id} from SQL database.")
class NoSQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting {data} into NoSQL database.")

    def update(self, record_id, data):
        print(f"Updating record {record_id} in NoSQL database with {data}.")

    def delete(self, record_id):
        print(f"Deleting record {record_id} from NoSQL database.")


sql_db = SQLDatabase()
sql_db.insert("User Data")
sql_db.update(101, "Updated User Data")
sql_db.delete(101)

nosql_db = NoSQLDatabase()
nosql_db.insert({"name": "John", "age": 30})
nosql_db.update("user_123", {"age": 31})
nosql_db.delete("user_123")
