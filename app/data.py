'''Module containing a Database class to hold the specs of randomized monsters.'''

from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    '''Class that holds a MongoDB database and collection of MonsterLab.Monster objects.'''

    def __init__(self):
        # Connect to database using credentials from .env
        load_dotenv()
        self.database = MongoClient(getenv("DB_URL"),tlsCAFile=where())["Bandersnatch"]
        self.collection = self.database.get_collection("Monsters")

    def seed(self, amount):
        '''Inserts a given number of MonsterLab.Monster objects into the Monster collection.'''
        self.collection.insert_many(
            [Monster().to_dict() for i in range(amount)])
        return f"Successfully inserted {amount} documents!"

    def reset(self):
        '''Deletes all documents in the collection.'''
        self.collection.delete_many({})

    def count(self) -> int:
        '''Returns number of documents in the collection.'''
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        '''Returns pandas DataFrame of documents in the collection.'''
        return DataFrame(self.collection.find({}, {"_id": False}))

    def html_table(self) -> str:
        '''Returns html table of documents in the collection.'''
        if self.count() == 0:
            return None
        return self.dataframe().to_html()
    
if __name__ == "__main__":
    db = Database()
    print(db.html_table())