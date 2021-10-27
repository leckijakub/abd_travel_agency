from app.models.database import db

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    # autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'))
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
        }
