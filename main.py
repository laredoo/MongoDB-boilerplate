from database import Database
import random

db_client = Database('TEST_DATABASE')

# database = db_client.get_database_client()

names = ['Laboratory A', 'Laboratory B', 'Laboratory C', 'Laboratory D', 'Laboratory E']
batches = ['A', 'B', 'C']
number_of_files = [10, 27, 30, 41]

documents = [
    {
        'name': laboratory,
        
        'terms': [
            {
            
                'batch': batch,
                
                'tests': random.choice(number_of_files)
        
            }
            for batch in batches
        ]
    }
    for laboratory in names
]

filter = {
    'terms': {
        '$elemMatch': {
            'tests': {'$gte': 40}
        }
    }
}

columns = {
    'name': 1
}

update = {
    '$set': {
        'Capability': random.randint(10, 100)
    }
}

new_doc = {
        'name': 'Laboratory F',
        
        'terms': [
            {
            
                'batch': batch,
                
                'tests': random.choice(number_of_files)
        
            }
            for batch in batches
        ]
    }

db_client.replace_document('LABORATORY_COLLECTION', '6619c117e805a1a39298114d', new_doc)

