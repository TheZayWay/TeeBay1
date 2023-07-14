from .db import db, environment, SCHEMA, add_prefix_for_prod

class Cart(db.Model):
    __tablename__ = 'carts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    teeshirts_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("teeshirts.id")))

    users = db.relationship("User", back_populates="carts")

    teeshirts = db.relationship(
        "Teeshirt",
        secondary="carts_teeshirts",
        back_populates="carts"
    )

    def to_dict(self):
        return {
            'id': self.id,
            'users_id': self.users_id,
            'teeshirts_id': self.teeshirts_id,
        }