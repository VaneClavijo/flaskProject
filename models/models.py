from App import db

class Equipment(db.Model):
    equipment_id=db.Column(db.Integer, primary_key=True,autoincrement=True,unique=True)
    equipment_name=db.Column(db.String(100),unique=True)


class Borrow(db.Model):
    borrow_id=db.Column(db.Integer, primary_key=True,autoincrement=True,unique=True)
    borrow_person=db.Column(db.String(50),nullable=False)
    borrow_start=db.Column(db.Date,nullable=False)
    borrow_end=db.Column(db.Date,nullable=False)
    borrow_delivery=db.Column(db.Date,nullable=False)
    borrow_state=db.Column(db.String(10),nullable=False)
    borrow_equipment=db.Column(db.Integer,nullable=False)

db.create_all()