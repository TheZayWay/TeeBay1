from flask.cli import AppGroup
from .users import seed_users, undo_users, seed_listing_users, undo_seed_listing_users
from .brands import seed_brands, undo_brands
from .carts import seed_carts_teeshirts, undo_seed_carts_teeshirts, undo_seed_carts
from .teeshirt import undo_seed_teeshirts
from .listings import undo_seed_listings
from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    if environment == 'production':
        undo_seed_listings()
        undo_seed_listing_users()
        undo_seed_teeshirts()
        undo_seed_carts_teeshirts()
        undo_seed_carts()
        undo_users()
        undo_brands()
    # seed_users()
    
    # seed_carts()    
    seed_carts_teeshirts()
    seed_listing_users()
    seed_brands()

@seed_commands.command('undo')
def undo():
    undo_seed_listings()
    undo_seed_listing_users()
    undo_seed_teeshirts()
    undo_seed_carts_teeshirts()
    undo_seed_carts()
    undo_users()
    undo_brands()
    
  