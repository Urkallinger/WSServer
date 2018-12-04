import pymongo

class MongoClient:
    """
    Client for accessing the MongoDB.

    Start: sudo service mongodb start
    Stop: sudo service mongodb stop
    """
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://192.168.178.29:27017/")
        self.db = self.client["TestDB"]
        self.users = self.db["users"]
    
    def getUsers(self):
        return self.users.find()
    
    def addUser(self):
        mylist = [{ "_id": 1, "name": "John", "address": "Highway 37"},
                  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
                  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
                  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
                  { "_id": 5, "name": "Michael", "address": "Valley 345"},
                  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
                  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
                  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
                  { "_id": 9, "name": "Susan", "address": "One way 98"},
                  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
                  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
                  { "_id": 12, "name": "William", "address": "Central st 954"},
                  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
                  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}]

        userIds = self.users.insert_many(mylist)
        print(userIds.inserted_ids)

    def deleteAllUsers(self):
        self.users.delete_many({})

if __name__ == "__main__":
    client = MongoClient()
    client.addUser()
    for doc in client.getUsers():
        print(doc)
    client.deleteAllUsers()