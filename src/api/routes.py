from flask import jsonify, request
from src.config import db
from src.models.book import Book

def init_api_routes(app):

    @app.route('/api/books', methods=['GET'])
    def get_books():
        books = db.session.query(Book).all()
        return jsonify([{'id': b.id, 'title': b.title, 'author': b.author, 'year': b.year} for b in books])

    @app.route('/api/books', methods=['POST'])
    def post_book():
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'], year=data.get('year'))
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'id': new_book.id, 'message': 'Creado'}), 201

    @app.route('/api/books/<int:book_id>', methods=['PUT'])
    def put_book(book_id):
        data = request.get_json()
        book = db.session.query(Book).get(book_id)
        if book:
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            db.session.commit()
            return jsonify({'message': 'Actualizado'}), 200
        return jsonify({'error': 'No encontrado'}), 404

    @app.route('/api/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        book = db.session.query(Book).get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return jsonify({'message': 'Eliminado'}), 204
        return jsonify({'error': 'No encontrado'}), 404