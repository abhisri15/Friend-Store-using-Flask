from app import db

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "role": self.role,
            "gender": self.gender,
            "description": self.description,
            "imgUrl": self.img_url,
        }
