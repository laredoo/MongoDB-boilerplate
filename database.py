from utils import BaseModel
from bson.objectid import ObjectId

class Database(BaseModel):
    def __init__(self, database_name):
        self.BaseModel = BaseModel()
        self.database_name = database_name

    def get_database_client(self):
        """ Get the database client from Base Model"""
        client = self.BaseModel.get_connection()
        print('{database} ACCESSED'.format(database=self.database_name))
        return client[self.database_name]
    
    def get_collection(self, collection_name):
        """ Get a collection inside of the database """
        db = self.get_database_client()
        collection = db[collection_name]
        print('{collection} ACCESSED'.format(collection=collection_name))
        return collection

    def create_collection(self, collection_name):
        """ Create a collection inside of the database """
        db = self.get_database_client()
        db.create_collection(collection_name)
        print('{collection} created'.format(collection=collection_name))

    def list_collections(self):
        """ List all the collections inside of the database """
        db = self.get_database_client()
        collections_names = db.list_collection_names()
        print(collections_names)

    # CREATE
    def insert_document(self, collection_name, document):
        """ Insert one document into a collection """
        collection = self.get_collection(collection_name)
        inserted_id = collection.insert_one(document).inserted_id
        print('The inserted ID of the document is {inserted_id}', inserted_id)

    # CREATE
    def insert_many_documents(self, collection_name, documents):
        """ Insert a list of documents into a collection """
        collection = self.get_collection(collection_name)
        inserted_ids = collection.insert_many(documents).inserted_ids
        print('The inserted ID of the documents are ', inserted_ids)

    # READ
    def find(self, collection_name, filter):
        """ Return a cursor to database find method """
        collection = self.get_collection(collection_name)
        return collection.find(filter)
    
    # READ
    def find_one(self, collection_name, filter):
        """ Return a dict to database find_one method """
        collection = self.get_collection(collection_name)
        if not (cursor:=collection.find_one(filter)):
            return 'No documents found'
        return cursor
    
    # READ
    def count(self, collection_name, filter):
        """ Return the count of documents in database collection """
        collection = self.get_collection(collection_name)
        return collection.count_documents(filter)
    
    # READ
    def get_by_id(self, collection_name, id):
        """ Return the cursor of documents in database collection for a given id"""
        collection = self.get_collection(collection_name)
        return collection.find(
            {
                "_id": ObjectId(id)
            }
        )
    
    # READ
    def project_columns(self, collection_name, filter, columns):
        """ Return the cursor with specified columns of documents in database collection for a given filter"""
        collection = self.get_collection(collection_name)
        return collection.find(
            filter,
            columns
        )
    
    # UPDATE
    def update_by_id(self, collection_name, id, update):
        """ Update a document by its own id"""
        collection = self.get_collection(collection_name)
        _id = ObjectId(id)
        collection.update_one(
            {
                '_id': _id
            },
            update
        )

    # UPDATE
    def update_documents(self, collection_name, filter, update):
        """ Update many documents"""
        collection = self.get_collection(collection_name)
        collection.update_many(
            filter,
            update
        )

    # UPDATE
    def replace_document(self, collection_name, id, new_doc):
        """ Replace document keeping it's ID"""
        collection = self.get_collection(collection_name)
        collection.replace_one(
            {
                "_id": ObjectId(id)
            },

            new_doc
        )

    # DELETE
    def delete_by_id(self, collection_name, id, new_doc):
        """ Delete a document by it's ID"""
        collection = self.get_collection(collection_name)
        collection.delete_one(
            {
                "_id": ObjectId(id)
            }
        )

    # DELETE
    def delete_by_id(self, collection_name, filter):
        """ Delete many documents"""
        collection = self.get_collection(collection_name)
        collection.delete_many(
            filter
        )