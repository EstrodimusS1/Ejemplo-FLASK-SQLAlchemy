from flask import Flask
from src.api.routes import init_api_routes
from src.config import db

app = Flask(__name__)

# Crea las tablas automáticamente al arrancar [cite: 82, 86, 88]
db.Base.metadata.create_all(db.engine)

init_api_routes(app)

if __name__ == '__main__':
    app.run(debug=True)