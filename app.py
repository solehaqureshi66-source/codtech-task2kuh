from flask import Flask, jsonify, request

app = Flask(_name_)

# temporary data storage
books = [
    {"id": 1, "title": "Python Basics", "author": "Guido"},
    {"id": 2, "title": "Data Structures", "author": "Mark"}
]

@app.route('/')
def home():
    return "Library REST API is running"

# get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# get book by id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# add new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        "id": books[-1]["id"] + 1,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

# update book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book["id"] == book_id:
            book["title"] = data["title"]
            book["author"] = data["author"]
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# delete book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted successfully"})
    return jsonify({"message": "Book not found"}), 404


if _name_ == '_main_':
    app.run(debug=True)\