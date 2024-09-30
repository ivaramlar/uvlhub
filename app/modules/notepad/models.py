from app import db

#En el modelo se crean las tablas que representan este nuevo modulo, en este caso se crea la tabla dela db llamada Notepad
#Es como crear una nueva entidad en spring boot

class Notepad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='notepads', lazy=True)

    def __repr__(self):
        return f'Notepad<{self.id}, Title={self.title}, Author={self.user.username}>'
