from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

mongo_uri = "mongodb://localhost:27017/desafio"
client = MongoClient(mongo_uri)
db = client["desafio"]

@app.route('/')
def index():
    
    try:
        db.command("ping")
        return "Bem-vindo ao Desafio de Palpites! MongoDB conectado com sucesso!"
    except Exception as e:
        return f"Bem-vindo ao Desafio de Palpites! Erro ao conectar ao MongoDB: {str(e)}"

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV') == 'development')