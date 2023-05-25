from flask import Flask
from .models import db
from .models.user import User, init_users_for_test
from .models.book import Book, init_books_for_test
from .models.borrow import Borrow, init_borrows_for_test
from .api.admin_handler import admin_handler
from .api.auth_handler import auth_handler
from .api.br_handler import br_handler
from .api.query_handler import query_handler

app = Flask(__name__)

def init_db_for_test():
    init_users_for_test()
    init_books_for_test()
    init_borrows_for_test()

def create_app(environment):
    app.config.from_object(environment)
    app.register_blueprint(admin_handler)
    app.register_blueprint(auth_handler)
    app.register_blueprint(br_handler)
    app.register_blueprint(query_handler)
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()
        init_db_for_test()
        return app
    return None