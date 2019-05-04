from exts import db
import shortuuid
import enum,datetime
from werkzeug.security import generate_password_hash,check_password_hash


class AdminModel(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11),nullable=True)
    _password = db.Column(db.String(100),nullable=True)
    email = db.Column(db.String(50))

    def __init__(self,*args,**kwargs):
        if "password" in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop("password")
        super(AdminModel, self).__init__(*args,**kwargs)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,newpwd):
        self._password = generate_password_hash(newpwd)

    def check_password(self,rawpwd):
        return check_password_hash(self._password,rawpwd)
