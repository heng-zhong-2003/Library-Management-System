from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from ..models.user import User
from ..models.book import Book
from ..models.borrow import Borrow
from ..models import db
from ..response import *

admin_handler = Blueprint(
    name='admin_handler',
    import_name=__name__,
    url_prefix='/api/admin'
)

@admin_handler.route(rule='/manage', methods=['POST'])
def admin_qualify():
    print('invoked')
    data = request.get_json(force=True)
    email = data.get('email', None)
    user = User.query.filter(
        User.email == email
    ).first()
    qualify = 'n'
    if user.role_id == 0:
        qualify = 'y'
    print(email, qualify)
    ret = {
        'qualified': qualify
    }
    return response_ok(data=ret)

@admin_handler.route(rule='/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    ret = [book.serialize() for book in books]
    return response_ok(data=ret)

@admin_handler.route(rule='/add_book', methods=['POST'])
def admin_add_book():
    data = request.get_json(force=True)
    isbn = data.get('isbn', None)
    title = data.get('title', None)
    author = data.get('author', None)
    total_stock = data.get('total_stock', None)
    book = Book.create(
        isbn=isbn,
        title=title,
        author=author,
        total_stock=total_stock,
        current_stock=total_stock
    )
    if book is None:
        return bad_request(msg='Book already exists')
    ret = book.serialize()
    return response_ok(data=ret)

@admin_handler.route(rule='/delete_book', methods=['POST'])
def admin_delete_book():
    data = request.get_json(force=True)
    isbn = data.get('isbn', None)
    book = Book.query.filter(
        Book.isbn == isbn
    ).first()
    if book is None:
        return bad_request(msg='Book to be deleted not found')
    borrows = Borrow.query.filter(
        Borrow.isbn == isbn
    ).all()
    try:
        for borrow_record in borrows:
            db.session.delete(borrow_record)
    except (SQLAlchemyError, IntegrityError) as e:
        db.session.rollback()
        print(f"Exception occurred during commit: {str(e)}")
        return bad_request(msg='Borrow records deletion failed')
    db.session.commit()
    book.delete()
    ret = book.serialize()
    return ret

@admin_handler.route(rule='/delete_user', methods=['POST'])
def admin_delete_user():
    data = request.get_json(force=True)
    email = data.get('email', None)
    user = User.query.filter(
        User.email == email
    ).first()
    if user is None:
        return bad_request(msg='User to be deleted not foune')
    borrows = Borrow.query.filter(
        Borrow.email == email
    ).all()
    try:
        for borrow_record in borrows:
            db.session.delete(borrow_record)
    except (SQLAlchemyError, IntegrityError) as e:
        db.session.rollback()
        print(f"Exception occurred during commit: {str(e)}")
        return bad_request(msg='Borrow records deletion failed')
    db.session.commit()
    user.delete()
    ret = user.serialize()
    return ret

@admin_handler.route(rule='/upgrade', methods=['POST'])
def admin_upgrade():
    data = request.get_json(force=True)
    email = data.get('email', None)
    ok = data.get('ok', None)
    if ok == 'y':
        print('upgraded')
        user = User.query.filter(
            User.email == email
        ).update({'role_id': 1})
        db.session.commit()
    ret = []
    return response_ok(data=ret)