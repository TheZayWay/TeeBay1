from app.models import db, Brand, Teeshirt, environment, SCHEMA
from sqlalchemy.sql import text

def seed_brands():
    # brand1 = Brand(
    #     name='Nike', teeshirts_id=1)
    # brand2 = Brand(
    #     name='Adidas', teeshirts_id=2)
    # brand3 = Brand(
    #     name='Nike', teeshirts_id=3)

    # db.session.add(brand1)
    # db.session.add(brand2)
    # db.session.add(brand3)
    # db.session.commit()
    # print("Brands have been seeded.")
    brand_data = [
        {'name': 'Nike', 'teeshirt_id': 1},
        {'name': 'Adidas', 'teeshirt_id': 2},
        {'name': 'Nike', 'teeshirt_id': 3},
        {'name': 'Nike', 'teeshirt_id': 4},
        {'name': 'Blue Mountain', 'teeshirt_id': 5},
        {'name': 'Hanes', 'teeshirt_id': 6}
    ]

    for brand_item in brand_data:
        brand = Brand(name=brand_item['name'])
        teeshirt_id = brand_item['teeshirt_id']
        brand.teeshirts_id = teeshirt_id
        db.session.add(brand)

    db.session.commit()
    print("Brands have been seeded.")

def undo_brands():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.brands RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM brands"))
        
    db.session.commit()
    print("Brands have been unseeded.")