from app.models import db, Teeshirt, Cart, environment, SCHEMA
from sqlalchemy.sql import text

def seed_carts_teeshirts(): 
    cart1 = Cart(users_id=1, teeshirts_id=1)
    cart2 = Cart(users_id=2, teeshirts_id=2)
    cart3 = Cart(users_id=3, teeshirts_id=3)

    teeshirt1 = Teeshirt(name="Nike Soccer Tee", type="Short Sleeve", description="Great for cold weather", brand="Nike", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPbRRjrAsC0qxUhbt-F8rRzl0dAndbCPcaWw&usqp=CAU", carts_id=1, user_id=1)
    teeshirt2 = Teeshirt(name="Adidas White Long Sleeve", type="Long Sleeve", description="Great for cold weather", brand="Adidas", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_GO6YTXGr1IAmWy7HyuuJiSjSDuMV0Jw9IA&usqp=CAU", carts_id=2, user_id=1)
    teeshirt3 = Teeshirt(name="Nike Fleece Long Sleeve", type="Fleece", description="Great for cold weather", brand="Nike", image_url="https://d3nt9em9l1urz8.cloudfront.net/media/catalog/product/cache/3/image/9df78eab33525d08d6e5fb8d27136e95/n/i/nibv2662-010_1.jpg", carts_id=3, user_id=2)
    teeshirt4 = Teeshirt(name="Short Sleeve Ever Henley", type="Button Short Sleeve", description="Great for cold weather", brand="Nike", image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjsur4ih1fh7S_b_HEXD09OKhgSahJFDQNbw&usqp=CAU", carts_id=1, user_id=2)
    teeshirt5 = Teeshirt(name="Blue Mountain Men Long Sleeve", type="Long Sleeve", description="Great for cold weather", brand="Blue Mountain", image_url="https://media.tractorsupply.com/is/image/TractorSupplyCompany/1294733?$456$", carts_id=2, user_id=3)
    teeshirt6 = Teeshirt(name="White Thermal", type="Thermal", description="Great for cold weather", brand="Hanes", image_url="https://i5.walmartimages.com/asr/f4ae820e-f55c-43f6-9555-e1cbc9897c3c.aef02fd3e7131997b02209193317fcce.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF", carts_id=3, user_id=3)

    cart1.teeshirts.extend([teeshirt1, teeshirt2])
    cart2.teeshirts.extend([teeshirt3, teeshirt4])
    cart3.teeshirts.extend([teeshirt5, teeshirt6])

    db.session.add_all([cart1, cart2, cart3, teeshirt1, teeshirt2, teeshirt3, teeshirt4, teeshirt5, teeshirt6])
    db.session.commit()
    print("carts_teeshirts have been seeded.")


def undo_seed_carts_teeshirts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.carts_teeshirts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM carts_teeshirts"))
        
    db.session.commit()
    print("carts_teeshirts have been unseeded.")

def undo_seed_carts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.carts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM carts"))
        
    db.session.commit()
    print("Carts have been unseeded.")











# def seed_carts():
#     cart1 = Cart(users_id=1)
#     cart2 = Cart(users_id=2)
#     cart3 = Cart(users_id=3)

#     db.session.add(cart1)
#     db.session.add(cart2)
#     db.session.add(cart3)
#     db.session.commit()
#     print("Carts have been seeded.")