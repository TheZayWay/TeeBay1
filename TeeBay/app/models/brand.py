from .db import db, environment, SCHEMA, add_prefix_for_prod


class Brand(db.Model):
    __tablename__ = 'brands'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    teeshirts_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("teeshirts.id")))
    

    teeshirts = db.relationship("Teeshirt", back_populates="brands")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'teeshirts_id': self.teeshirts_id
        }