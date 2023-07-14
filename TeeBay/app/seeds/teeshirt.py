from app.models import db, Teeshirt, environment, SCHEMA
from sqlalchemy.sql import text


def undo_seed_teeshirts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.teeshirts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM teeshirts"))
        
    db.session.commit()
    print("Teeshirts have been unseeded.")


# def seed_teeshirts():
#     teeshirt1 = Teeshirt()
#     teeshirt2 = Teeshirt()
#     teeshirt3 = Teeshirt()

#     db.session.add(demo)
#     db.session.add(marnie)
#     db.session.add(bobbie)
#     db.session.commit()
#     print("Teeshirts have been seeded.")