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

