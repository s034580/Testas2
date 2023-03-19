from app import db


class Bills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    group = db.relationship("Groups")

    def __init__(self, group_id, name, amount):
        self.group_id = group_id
        self.name = name
        self.amount = amount
