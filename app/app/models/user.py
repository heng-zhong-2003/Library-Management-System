from . import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

class User(db.Model):
    __tablename__ = 'user'
    #id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    role_id = db.Column(db.Integer)     # 0: admin, 1: member, 2: normal
    email = db.Column(db.String(80), primary_key=True, unique=True)
    
    @classmethod
    def create(cls, email, password, name, role_id=2):
        new_user = None
        try:
            new_user = User(
                email = email,
                password = password,
                name = name,
                role_id = role_id
            )
            db.session.add(new_user)
            db.session.commit()
        except db.exc.IngegrityError:
            db.session.rollback()
            print('Email already exist')
        return new_user
    
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
        user_dict = {
            'email': self.email,
            'name': self.name,
            'password': self.password,
            'role_id': self.role_id
        }
        return user_dict
    
    def __str__(self):
        return str(self.serialize())

def init_users_for_test():
    print('init users for test')
    db.session.add(
        User(
            email='hzhongfdu@gmail.com',
            name='Kagura_Hitoha',
            password='123456',
            role_id=0
        )
    )
    db.session.add(
        User(
            email='yamamoto@gmail.com',
            name='Yamamoto',
            password='123456',
            role_id=2
        )
    )
    db.session.add(
        User(
            email='iwanami@gmail.com',
            name='Iwanami',
            password='123456',
            role_id=1
        )
    )