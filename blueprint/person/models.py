from blueprint.app import db


class Person(db.Model):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f"<Person: {self.name}>"
    
    def get_id(self):
        return self.id