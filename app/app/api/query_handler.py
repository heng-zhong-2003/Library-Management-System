from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from ..models.user import User
from ..models.book import Book
from ..models.borrow import Borrow
from ..models import db
from ..response import *

query_handler = Blueprint (
    name='query_handler',
    import_name=__name__,
    url_prefix='/api/query'
)

@query_handler.route(rule='/search_title', methods=['POST'])
def query_search_title():
    data = request.get_json(force=True)
    title = data.get('title')
    books = Book.query.filter(
        Book.title.like('%'+title+'%')
    ).all()
    # print(books[0].title)
    ret = [book.serialize() for book in books]
    return response_ok(data=ret)

@query_handler.route(rule='/search_username', methods=['POST'])
def query_search_username():
    data = request.get_json(force=True)
    name = data.get('name', None)
    users = User.query.filter(
        User.name.like('%'+name+'%')
    ).all()
    ret = [user.serialize() for user in users]
    return response_ok(data=ret)

@query_handler.route(rule='/borrows', methods=['POST'])
def query_borrows():
    data = request.get_json(force=True)
    email = data.get('email')
    print(email)
    borrows = Borrow.query.filter(
        Borrow.email == email
    ).all()
    books = []
    for borrow in borrows:
        book = Book.query.filter(
            Book.isbn == borrow.isbn
        ).first()
        books.append(book)
    ret = [bk.serialize() for bk in books]
    for s in ret:
        print(s)
    return response_ok(data=ret)