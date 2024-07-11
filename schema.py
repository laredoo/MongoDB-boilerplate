from database import Database

book_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["title", "authors", "publish_date", "type", "copies"],
        "properties": {
            "title": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "authors": {
                "bsonType": "array",
                "items": {
                    "bsonType": "array",
                    "description": "must be an objectID and is required"
                }
            },
            "publish_date": {
                "bsonType": "date",
                "description": "must be a date and is required"
            },
            "type": {
                "enum": ["Fiction", "Non-Fiction"],
                "description": "must be only one and is required"
            },
            "copies": {
                "bsonType": "int",
                "minimum": 0,
                "description": "must be a integer greater than 0 and is required"
            },
        }
    }
}

class ModelSchema():
    def __init__(self, db, collection_name):
        self.db = db
        self.collection_name = collection_name
        self.collection = self.db.get_collection(collection_name)

    def set_validator(self, validator):
        db_client = self.db.get_database_client()
        db_client.command('collMod', self.collection_name, validator=validator)
        print('{collection} ACCESSED and validator SET'.format(collection=self.collection_name))

db_client = Database('TEST_DATABASE')

"""try:
    db_client.create_collection('BOOK_COLLECTION')
except Exception as e:
    print(e)"""

schema = ModelSchema(db_client, 'BOOK_COLLECTION')

schema.set_validator(book_validator)


