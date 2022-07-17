import pymongo

client = pymongo.MongoClient("mongodb+srv://vijaysankar117:Vijay_248621@vijcluster0.0phlp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)
d={
    "name":"vijay",
    "email":"vijay117@gmail.com",
    "surname":"Lalam"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
d={
    "name":"vijay",
    "email":"vijay117@gmail.com",
    "surname":"Lalam"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)d={
    "name":"vijay",
    "email":"vijay117@gmail.com",
    "surname":"Lalam"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)

