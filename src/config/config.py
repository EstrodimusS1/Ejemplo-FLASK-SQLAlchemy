import os

class Config:
    # Esta es la ruta de tu base de datos
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///biblioteca.db')