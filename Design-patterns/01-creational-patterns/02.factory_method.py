from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def execute(self):
        pass
        

class MySql(Database):
    def connect(self):
        print("Connected to MySQL")
    def execute(self, query):
        return f"Executing {query} in MySQl"

class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB")
    def execute(self, query):
        return f"Executing {query} in MongoDB"

class DatabaseFactory:
    @staticmethod
    def getDatabase(dbname) -> Database:
        if dbname=="mysql":
            return MySql()
        elif dbname=="mongo":
            return MongoDB()
        else:
            raise "Unable to get the database"

def executeQuery(dbName, query):
    db = DatabaseFactory.getDatabase(dbName)
    print(id(db))
    db.connect()
    print(db.execute(query))

executeQuery("mysql", "select * from table")
executeQuery("mongo", "{user: {query}}")


    
    