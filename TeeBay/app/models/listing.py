from .db import db, environment, SCHEMA, add_prefix_for_prod

listings_users = db.Table(
    "listings_users",
    db.Column("listings_id", db.Integer, db.ForeignKey(add_prefix_for_prod("listings.id")), primary_key=True),
    db.Column("users_id", db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), primary_key=True)
)

class Listing(db.Model):
    __tablename__ = 'listings'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    teeshirts_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("teeshirts.id")))
    users_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    
    teeshirts = db.relationship("Teeshirt", back_populates="listings")
    users = db.relationship(
        "User",
        secondary="listings_users",
        back_populates="listings"
    )

    def to_dict(self):
        return {
            'id': self.id,
            'users_id': self.users_id,
            'teeshirts_id': self.teeshirts_id
        }
