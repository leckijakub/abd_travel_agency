from app.models.database import db
import enum

class employee_type(enum.Enum):
    Administrator = 1
    Animator = 2
    Service_organizer = 3
    Reservation_empolyee = 4

class Employee(db.Model):
    __tablename__ = "Employee"
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Enum(employee_type), nullable=False)
