import json
from pydoc import doc
from pymongo import MongoClient, InsertOne
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os


class ScriptsMongoDB:
    def __init__(self) -> None:
        super().__init__()

        load_dotenv()

        user = os.getenv("DB_MONGO_USER")
        password = os.getenv("DB_MONGO_PASSWORD")
        cluster_name = os.getenv("DB_MONGO_CLUSTER")

        dbname = os.getenv("DB_MONGO_NAME")

        # self.client = MongoClient("mongodb+srv://{}:{}@{}.tirlce4.mongodb.net/?retryWrites=true&w=majority".format(
        #    user,
        #    password,
        #    dbname,
        #    cluster_name
        # ))
        self.client = MongoClient(
            "mongodb://root:pass@mongo:27017/?authMechanism=DEFAULT"
        )
        self.db = self.client[dbname]

    def create_id(self):
        return ObjectId()

    def send_json_to_db(self, *args, **kwargs) -> None:
        if "path_json" in kwargs and "collection_name" in kwargs:
            path_json = kwargs["path_json"]
            collection_name = kwargs["collection_name"]

            collection = self.db[collection_name]

            requesting = []

            with open(path_json) as json_file:
                list_dict = json.load(json_file)
                for data_dict in list_dict:
                    requesting.append(InsertOne(data_dict))

            try:
                collection.bulk_write(requesting)
            except Exception as e:
                print(e)

    def delete_elements_from_collection(self, *args, **kwargs):
        if "collection_name" in kwargs:
            collection_name = kwargs["collection_name"]
            collection = self.db[collection_name]

            collection.remove()

    def create_collection(self, *args, **kwargs):
        if "collection_name" in kwargs:
            collection_name = kwargs["collection_name"]

            self.db.create_collection(collection_name)

    def list_collections(self, *args, **kwargs):
        return self.db.list_collection_names()

    def verify_collection_in_db(self, *args, **kwargs):
        if "collection_name" in kwargs:
            collection_name = kwargs["collection_name"]
            list_of_collection = self.list_collections()

            return collection_name in list_of_collection

        return False

    def get_collection(self, *args, **kwargs):
        collection_name = kwargs["collection_name"]

        return_limit = 100 if "return_limit" not in kwargs else kwargs["return_limit"]

        if self.verify_collection_in_db(**kwargs):
            documents = (
                self.db.get_collection(collection_name).find({}).limit(return_limit)
            )
            return documents

    def get_collection_data(self, *args, **kwargs):
        if "collection_name" in kwargs:
            collection_name = kwargs["collection_name"]

            return_limit = (
                100 if "return_limit" not in kwargs else kwargs["return_limit"]
            )

            if self.verify_collection_in_db(**kwargs):
                documents = (
                    self.db.get_collection(collection_name).find({}).limit(return_limit)
                )

                arr_doc = []

                for document in documents:
                    arr_doc.append(document)

                return arr_doc

    def get_data_find(self, *args, **kwargs):
        if "collection_name" in kwargs and "filter" in kwargs:
            collection_name = kwargs["collection_name"]
            filter = kwargs["filter"]

            objs = self.db[collection_name].find(filter)

            dict_objs = []
            for obj in objs:
                dict_objs.append(obj)

            return dict_objs

        return []

    def get_object_by_id(self, *args, **kwargs):
        if "collection_name" in kwargs and "_id" in kwargs:
            collection_name = kwargs["collection_name"]
            _id = kwargs["_id"]
            objInstance = ObjectId(_id)
            object_found = self.db[collection_name].find_one({"_id": objInstance})

            return object_found

    def number_elements_collection(self, *args, **kwargs):
        if "collection_name" in kwargs:
            collection_name = kwargs["collection_name"]

            if self.verify_collection_in_db(**kwargs):
                return self.db[collection_name].find().count()

        return 0

    def close_connection(self, *args, **kwargs):
        self.client.close()

    def insert_object(self, *args, **kwargs):
        if "collection_name" in kwargs and "object" in kwargs:
            collection_name = kwargs["collection_name"]
            object_to_insert = kwargs["object"]
            new_object = [InsertOne(object_to_insert)]

            collection_gestores = self.db[collection_name]

            collection_gestores.bulk_write(new_object)

            return {"status": 200, "id": object_to_insert["_id"]}

        return {"status": 400}
