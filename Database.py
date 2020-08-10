class Resource:
    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    def collection():
        return self.db[self.collection]

    def create(data):
        return self.collection().insert(data)
    
    def find(where = {}):
        return self.collection().find(where)
    
    def delete(where = {}):
        return self.collection().remove(where)
    
    def update(patch, where={}, upsert=False):
        return self.collection().update(patch, where, upsert=upsert)

class MongoDatabase:
    def __init__(self, db):
        self.movies = Resource(db, "movies")
        self.series = Resource(db, "series")
        self.seasons = Resource(db, "seasons")
        self.episodes = Resource(db, "episodes")
        self.people = Resource(db, "people")
        self.keywords = Resource(db, "keywords")
        self.tv_networks = Resource(db, "tv_networks")
        self.production_companies = Resource(db, "production_companies")
        self.collections = Resource(db, "collections")