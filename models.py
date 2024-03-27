from bson import ObjectId
from db import db

def add_algorithm(name, type, description):
    try:
        algorithm = {"Nume": name, "Tip": type, "Descriere": description}
        result = db["algorithms"].insert_one(algorithm)
        return str(result.inserted_id)
    except Exception as e:
        print(f"Error adding algorithm: {e}")
        return None

def get_algorithms():
    try:
        algorithms = list(db["algorithms"].find({}))
        for alg in algorithms:
            alg['_id'] = str(alg['_id'])
        return algorithms
    except Exception as e:
        print(f"Error getting algorithms: {e}")
        return []

def add_key(algorithm_id, key_value, creation_date, expiration_date=None):
    try:
        key = {
            "AlgoritmID": algorithm_id, 
            "Cheie": key_value, 
            "DataCreare": creation_date, 
            "DataExpirare": expiration_date
        }
        result = db["keys"].insert_one(key)
        return str(result.inserted_id)
    except Exception as e:
        print(f"Error adding key: {e}")
        return None

def get_keys():
    try:
        keys = list(db["keys"].find({}))
        for key in keys:
            key['_id'] = str(key['_id'])
        return keys
    except Exception as e:
        print(f"Error getting keys: {e}")
        return []

def add_file(file_name, file_path, key_id):
    try:
        file_record = {
            "file_name": file_name,
            "file_path": file_path,
            "cheie_id": ObjectId(key_id),
        }
        result = db["files"].insert_one(file_record)
        return str(result.inserted_id)
    except Exception as e:
        print(f"Error adding file: {e}")
        return None

def get_files():
    try:
        files = list(db["files"].find({}))
        for file in files:
            file['_id'] = str(file['_id'])
        return files
    except Exception as e:
        print(f"Error getting files: {e}")
        return []
