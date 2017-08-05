from pymongo import MongoClient
from config import Config
from src.db.db_constants import Databases, Collections
from src.errors.errors import InvalidCollection, InvalidDatabase
import src.utils.logger as logger


class DbConnection:
    def __init__(self):
        self._client = MongoClient(Config().db_url)
        self._db = self._client[Databases().kapitol]
        self._database_names = Databases()
        self._collection_names = Collections()

    def _get_collection(self, collection_name):
        if not self._collection_names.is_collection_valid(collection_name):
            raise InvalidCollection('The collection: ' + collection_name, ' is not valid')
        return self._db[collection_name]

    def insert(self, document, collection_name):
        collection = self._get_collection(collection_name)
        try:
            collection.insert_one(document)
        except Exception as e:
            # TODO: handle this error
            logger.error('Inserting document:', document, 'into collection:', collection_name)
            raise e
        return None

    def find(self, collection_name, params=None):
        collection = self._get_collection(collection_name)
        try:
            result = collection.find(params)
        except Exception as e:
            # TODO: handle this error
            logger.error('finding document with filter:', params, 'in collection:', collection_name)
            raise e
        return result

    def update(self, collection_name, params, document, upsert=False):
        collection = self._get_collection(collection_name)
        try:
            collection.update_one(filter=params, update=document, upsert=upsert)
        except Exception as e:
            # TODO: handle this error
            logger.error('Inserting document:', document, 'into collection:', collection_name)
            raise e
        return None


db = DbConnection()


def insert(document, collection_name):
    return db.insert(document, collection_name)


def find(collection_name, params=None):
    return db.find(collection_name, params)


def update(collection_name, params, document, upsert=False):
    db.update(collection_name, params, document, upsert)
