from pymongo import MongoClient, InsertOne,ReturnDocument
from bson.objectid import ObjectId
import json

conn = MongoClient("mongodb://root:pass@localhost:27017/?authMechanism=DEFAULT");
db = conn.BaseAlfa2
collection = db.cidade

def insert():
    cidade = {
        "nome":"São José dos Campos",
        "estado":"São Paulo",
        "sigla":"",
        "cod_ibge":3549904
    }

    collection.insert_one(cidade)
    return cidade


def update():
    return collection.find_one_and_update(
    {"cod_ibge":3549904},
    {"$set": {"sigla": "SP"}},
    upsert=True,
    return_document=ReturnDocument.AFTER)


def delete():
    collection.delete_one(
        {"cod_ibge":3549904}
    )
    return None

def get():
    return collection.find_one({"cod_ibge":3549904})

def test_insert():   
    assert sorted(insert().items()) == sorted(get().items())

def test_update():
    assert sorted(update().items()) == sorted(get().items())
    
def test_delete():
    assert delete() == get()
