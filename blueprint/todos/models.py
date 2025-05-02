from blueprint.app import db


class Todo(db.Model):
    __tablename__ = "todos"

    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.Text, nullable=False)
    description     = db.Column(db.Text)
    is_active       = db.Column(db.Boolean)

    def __repr__(self):
        return f"<Task: {self.title} is {self.is_active}>"
    
    def get_id(self):
        return self.id