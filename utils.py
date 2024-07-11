from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

class BaseModel():
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.password = os.environ.get('MONGODB_PWD')
        self.connection_string = "mongodb+srv://devlucaslaredo:{password}@testcluster.7vp7zkm.mongodb.net/?retryWrites=true&w=majority&appName=testCluster"

    def get_connection(self):
        client = MongoClient(self.connection_string.format(password=self.password))
        if client:
            print('Client Connection STABLISHED')
            return client
        print('Client Connection FAILED')

    def list_databases(self):
        client = self.get_connection()
        print(client.list_database_names())


