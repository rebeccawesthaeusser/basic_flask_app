import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/database")
db = client["database"]
test_user_collection = db['test_user']

def find_user(username):
    found_user = test_user_collection.find_one({"name": username})
    if found_user is None:
        return " can't be found."
    else:
        return ""

def add_user(username):
   found_user = find_user(username)

   if found_user != "":
       test_user_collection.insert_one({"name": username, "age": None})
       return " has been added."
   else:
       return " has already been added."

def delete_user(username):
    found_user = find_user(username)

    if found_user == "":
        test_user_collection.delete_one({"name": username})
        return " has been deleted."
    else:
        return " couldn't be deleted."


def update_user(username, age):
    found_user = find_user(username)

    if found_user == "":
        if age is not None:
            select_user = {"name": username}
            update_query = {"$set": {"age": age}}
            test_user_collection.update_one(select_user, update_query)
            return " has been updated."
        else:
            return " hasn't been updated. Please enter the age."
    else:
        return " can't be found."

