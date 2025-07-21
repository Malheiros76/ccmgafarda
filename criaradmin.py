from pymongo import MongoClient
import bcrypt

client = MongoClient("mongodb+srv://bibliotecaluizcarlos:terra166@cluster0.uyvqnek.mongodb.net/?retryWrites=true&w=majority")
db = client["fardasDB"]
usuarios_col = db["usuarios"]

usuario_admin = "admin"
senha_admin = "cclcm2025"

senha_hash = bcrypt.hashpw(senha_admin.encode(), bcrypt.gensalt())

if usuarios_col.find_one({"usuario": usuario_admin}):
    print(f"Usuário '{usuario_admin}' já existe.")
else:
    usuarios_col.insert_one({
        "usuario": usuario_admin,
        "senha": senha_hash.decode('utf-8'),
        "nivel": "admin"
    })
    print(f"Usuário '{usuario_admin}' criado com sucesso.")
