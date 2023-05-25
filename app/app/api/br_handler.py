# ------------- borrow return handler -------------------------
from flask import Blueprint, request
from ..models.user import User
from ..models.book import Book
from ..models.borrow import Borrow
from ..models import db
from ..response import *

br_handler = Blueprint(
    name='borrow_return_handler',
    import_name=__name__,
    url_prefix='/api/borrow_return'
)

@br_handler.route(rule='/borrow', methods=['POST'])
def br_borrow():
    data = request.get_json(force=True)
    # role_id = data.get('role_id', None)
    isbn = data.get('isbn', None)
    email = data.get('email', None)
    # print(email)
    book = Book.query.filter(
        Book.isbn == isbn,
        Book.current_stock >= 1
    ).first()
    user = User.query.filter(
        User.email == email
    ).first()
    print(email)
    role_id = user.role_id
    # print(user.serialize())
    if book is None:
        return bad_request(msg='Currently no stock')
    tot_borrow = Borrow.query.filter(
        Borrow.email == email
    ).count()       # ------------------- is .count() used like this? ---------------------------
    if role_id == 2 and tot_borrow >= 5:
        return bad_request(msg='Current borrows exceed limit for normal users')
    book.current_stock = book.current_stock - 1
    borrow = Borrow.create(
        email=email,
        isbn=isbn,
        borrow_time=db.func.current_timestamp()
    )
    if borrow is None:
        return bad_request(msg='Cannot borrow two same books')
    ret = borrow.serialize()
    return response_ok(data=ret)

@br_handler.route(rule='/return', methods=['POST'])
def br_return():
    data = request.get_json(force=True)
    # role_id = data.get('role_id', None)
    isbn = data.get('isbn', None)
    email = data.get('email', None)
    book = Book.query.filter(
        Book.isbn == isbn,
        Book.current_stock < Book.total_stock
    ).first()
    if book is None:
        return bad_request(msg='All collection of this book returned')
    book.current_stock = book.current_stock + 1
    borrow = Borrow.query.filter(
        Borrow.email == email,
        Borrow.isbn == isbn
    ).first()
    borrow.delete()
    ret = borrow.serialize()
    return response_ok(data=ret)
    