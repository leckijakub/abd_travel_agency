# -*- coding: utf-8 -*-
from app.models.database import db
from app.models.book import Book
from flask import render_template, request, jsonify

def index():
    book_id = request.args.get('id')
    if book_id is not None:
        book = db.session.query(Book).get(int(book_id))
        if book is not None:
            return jsonify(Book.query.get(int(book_id)).serialize)
        else:
            return f"No book with id = {book_id}."
    else:
        return render_template('book/books.html', books=[book.serialize for book in Book.query.all()])
        # return jsonify([book.serialize for book in Book.query.all()])

def store(title):
    book = Book(title=title)
    db.session.add(book)
    db.session.commit()
    return jsonify(book.serialize)

def update(book_id):
    new_title = request.args.get('title')
    try:
        book = db.session.query(Book).get(int(book_id))
        if book is not None:
            book.title = new_title
            db.session.commit()
        else:
            return f"Book with id = \"{book_id}\" doesn't exist."
    except Exception as e:
        db.session.rollback()
        raise e
    return "Book updated"

def delete(book_id):
    try:
        book = db.session.query(Book).get(int(book_id))
        if book is not None:
            db.session.delete(book)
            db.session.commit()
        else:
            return f"Book with id = \"{book_id}\" doesn't exist."
    except Exception as e:
        db.session.rollback()
        raise e
    return "Book deleted"    
