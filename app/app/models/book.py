from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from . import db

class Book(db.Model):
    __tablename__ = 'book'
    isbn = db.Column(db.String(30), primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    total_stock = db.Column(db.Integer)
    current_stock = db.Column(db.Integer)
    
    @classmethod
    def create(cls, isbn, title, author, total_stock=0, current_stock=total_stock):
        new_book = None
        try:
            new_book = Book(
                isbn = isbn,
                title = title,
                author = author,
                total_stock = total_stock,
                current_stock = current_stock
            )
            db.session.add(new_book)
            db.session.commit()
        except db.exc.IntegrityError:
            db.session.rollback()
            print('Book already exist')
        return new_book
    
    def commit(self):
        try:
            db.session.commit()
            return True
        except (SQLAlchemyError, IntegrityError) as e:
            db.session.rollback()
            print(f"Exception occurred during commit: {str(e)}")
            return False
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except (SQLAlchemyError, IntegrityError) as e:
            db.session.rollback()
            print(f"Exception occurred during commit: {str(e)}")
            return False
    
    def serialize(self):
        message_dict = {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'total_stock': self.total_stock,
            'current_stock': self.current_stock
        }
        return message_dict
    
    def __str__(self):
        return str(self.serialize())

def init_books_for_test():
    print('init books for test')
    db.session.add(
        Book(
            isbn='9780262510875',
            title='Structure and Interpretation of Computer Programs',
            author='Harnold Abelson',
            total_stock=5,
            current_stock=5
        )
    )
    db.session.add(
        Book(
            isbn='9783540642435',
            title='Elements of Mathematics, Algebra I',
            author='Nicolas Bourbaki',
            total_stock=4,
            current_stock=3
        )
    )
    db.session.add(
        Book(
            isbn='9781119061953',
            title='The Probabilistic Method',
            author='Noga Alon',
            total_stock=4,
            current_stock=3
        )
    )
    db.session.add(
        Book(
            isbn='9780521424264',
            title='Computational Complexity: A Modern Approach',
            author='Sanjeev Arora',
            total_stock=4,
            current_stock=4
        )
    )
    db.session.add(
        Book(
            isbn='9780262560993',
            title='The Little Schemer',
            author='Daniel Friedman',
            total_stock=5,
            current_stock=5
        )
    )
    db.session.add(
        Book(
            isbn='9780262046305',
            title='Introduction to Algorithms',
            author='Thomas Cormen',
            total_stock=3,
            current_stock=3
        )
    )
    db.session.commit()