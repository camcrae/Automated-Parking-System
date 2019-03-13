from application import db
from application.models import Customer, Reservation, PaymentMethod

db.create_all()

print("DB created.")
