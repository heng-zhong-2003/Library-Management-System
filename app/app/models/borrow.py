from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from . import db

class Borrow(db.Model):
    __tablename__ = 'Borrow'
    email = db.Column(db.String(80),db.ForeignKey('user.email') ,primary_key=True)
    isbn = db.Column(db.String(30), db.ForeignKey('book.isbn'), primary_key=True)
    borrow_time = db.Column(db.db.DateTime(), default = db.func.current_timestamp())
    
    @classmethod
    def create(cls, email, isbn, borrow_time):
        new_borrow = None
        try:
            new_borrow = Borrow(
                email = email,
                isbn = isbn,
                borrow_time = borrow_time
            )
            db.session.add(new_borrow)
            db.session.commit()
        except db.exc.IntegrityError:
            db.session.rollback()
            print('Unable to Borrow')
        return new_borrow
    
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
            'email': self.email,
            'isbn': self.email,
            'borrow_time': str(self.borrow_time)
        }
        return message_dict
    
    def __str__(self):
        return str(self.serialize())

def init_borrows_for_test():
    print('init borrows for test')
    db.session.add(
        Borrow(
            email='yamamoto@gmail.com',
            isbn='9783540642435',
            borrow_time='2023-01-01 00:00:10'
        ),
        Borrow(
            email='yamamoto@gmail.com',
            isbn='9781119061953',
            borrow_time='2023-01-01 00:00:10'
        )
    )
    db.session.commit()