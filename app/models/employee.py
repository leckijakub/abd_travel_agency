from app.models.database import db
import enum

class employee_type(enum.Enum):
    Administrator = 1
    Animator = 2
    Service_organizer = 3
    Reservation_empolyee = 4

class Employee(db.Model):
    __tablename__ = "Employee"
    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    user = db.relationship('User', back_populates='employee')
    position = db.Column(db.Enum(employee_type), nullable=False)
    created_reservations = db.relationship("Reservations")
