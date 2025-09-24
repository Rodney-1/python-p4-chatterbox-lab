from app import app
from models import db, Message

with app.app_context():
    print("Seeding messages...")

    db.session.query(Message).delete()

    m1 = Message(body="Hello World!", username="Ian")
    m2 = Message(body="This is a test message.", username="Sam")
    m3 = Message(body="Flask is awesome!", username="Jamie")

    db.session.add_all([m1, m2, m3])
    db.session.commit()

    print("Seed complete.")
