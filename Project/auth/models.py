from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from base_model import db
class User(UserMixin, db.Model):
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), unique=True, index=True)
    password_hash = db.Column(db.String(150))
    roles = db.relationship("UserRoles", back_populates="user")
    account = db.relationship("Account", back_populates="user")

    def __init__(self, id, email, username, roles = []):
        self.id = id
        self.email = email
        self.username = username
        # pseudo-serializer for loading from json (map dict role to Role)
        if roles and type(roles[0]) == dict:
            from roles.models import Role
            roles = [Role(**r) for r in roles]
        self.roles = roles
        self.authenticated = False
    def is_active(self):
        return self.is_active()
    def is_anonymous(self):
        return False
    def is_authenticated(self):
        return self.authenticated
    def is_active(self):
        return True
    def get_id(self):
        return str(self.id)
    def has_role(self, role):
        for assoc in self.roles:
            if assoc.role.name == role:
                return True
        return False
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    name = db.Column(db.String(30), index=True, unique=True)
    users = db.relationship("UserRoles", back_populates="role")


# https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#association-object
class UserRoles(db.Model):
    __table_args__ = (db.UniqueConstraint('user_id', 'role_id'),)
    user_id = db.Column(db.ForeignKey('is601_user.id'))
    role_id = db.Column(db.ForeignKey('is601_role.id'))
    # extra_data = db.Column(String(50))
    role = db.relationship("Role", back_populates="users")
    user = db.relationship("User", back_populates="roles")