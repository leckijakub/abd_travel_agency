from app.models.database import db
from app.models.user import User
import enum

class employee_type(enum.Enum):
    Administrator = 1
    Animator = 2
    Service_organizer = 3
    Reservation_empolyee = 4

class Employee(User):
    __tablename__ = "Employee"
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    position = db.Column(db.Enum(employee_type), nullable=False)
    created_reservations = db.relationship("Reservation")

    __mapper_args__ = {
        'polymorphic_identity':'Employee',
    }
