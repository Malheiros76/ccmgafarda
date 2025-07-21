from pymongo import MongoClient

client = MongoClient("mongodb+srv://bibliotecaluizcarlos:terra166@cluster0.uyvqnek.mongodb.net/?retryWrites=true&w=majority")
db = client["fardasDB"]

usuarios_col = db["usuarios"]

# Atualiza nível do admin
usuarios_col.update_one(
    {"usuario": "admin"},
    {"$set": {"nivel": "admin"}}
)

print("Admin atualizado para nível admin.")
