from pymongo import MongoClient
import bcrypt

# Conexão MongoDB (mesma que no seu app)
client = MongoClient("mongodb+srv://bibliotecaluizcarlos:terra166@cluster0.uyvqnek.mongodb.net/?retryWrites=true&w=majority")
db = client["fardasDB"]
usuarios_col = db["usuarios"]

def hash_senha(senha):
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

def criar_usuario_admin(usuario, senha):
    senha_hash = hash_senha(senha).decode('utf-8')
    if usuarios_col.find_one({"usuario": usuario}):
        print(f"Usuário '{usuario}' já existe.")
    else:
        usuarios_col.insert_one({
            "usuario": usuario,
            "senha": senha_hash,
            "nivel": "admin"
        })
        print(f"Usuário admin '{usuario}' criado com sucesso!")

if __name__ == "__main__":
    usuario = input("Nome do usuário admin que deseja criar: ")
    senha = input("Senha para o usuário admin: ")
    criar_usuario_admin(usuario, senha)
