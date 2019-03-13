from application import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fn = db.Column(db.String(128), index=True, unique=False)
    ln = db.Column(db.String(128), index=True, unique=False)
    vInfo = db.Column(db.String(128), index=True, unique=False)
    dur = db.Column(db.Integer, index=True, unique=False)
    reservations = db.RelationshipProperty('Reservation', backref='customer', lazy=True)
    payment_methods = db.RelationshipProperty('PaymentMethod', backref='customer', lazy=True)
    
    # def __init__(self, id, dur, vInfo, ln, fn):
    #     self.id = id
    #     self.dur = dur
    #     self.vInfo = vInfo
    #     self.ln = ln
    #     self.fn = fn

    def __repr__(self):
        return '<Customer ID %r>' % self.id


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    checkin = db.Column(db.TIMESTAMP, index=True, unique=False)
    checkout = db.Column(db.TIMESTAMP, index=True, unique=False)
    car_position = db.Column(db.Integer, index=True, unique=False)
    approx_checkin = db.Column(db.TIMESTAMP, index=True, unique=False)
    approx_checkout = db.Column(db.TIMESTAMP, index=True, unique=False)
    status = db.Column(db.String(128), index=True, unique=False)
    payment_method = db.RelationshipProperty('PaymentMethod', uselist=False, backref='reservation', lazy=True)

    def __init__(self, id, customer_id, checkin, checkout, car_position, approx_checkin, approx_checkout, status):
        self.id = id
        self.customer_id = customer_id
        self.checkin = checkin
        self.checkout = checkout
        self.approx_checkin = approx_checkin
        self.approx_checkout = approx_checkout
        self.status = status

    def __repr__(self):
        return '<Reservation ID %r>' % self.id


class PaymentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'))
    card_number = db.Column(db.String(128), index=True, unique=False)
    exp_date = db.Column(db.String(128), index=True, unique=False)
    csc = db.Column(db.String(128), index=True, unique=False)

    def __init__(self, customer_id, card_number, exp_date, csc):
        self.id = id
        self.customer_id = customer_id
        self.card_number = card_number
        self.exp_date = exp_date
        self.csc = csc

    def __repr__(self):
        return '<Payment ID %r>' % self.id
