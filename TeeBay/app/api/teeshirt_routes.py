from flask import Blueprint, jsonify, session, request, render_template, redirect
from flask_login import current_user
from app.models import db, Teeshirt, User
from app.forms.selling_form import SellingForm

teeshirt_routes = Blueprint('teeshirt', __name__)

# GET ROUTES 

#Get all teeshirts
@teeshirt_routes.route('/', methods=['GET'])
def get_all_teeshirts():
    teeshirts = Teeshirt.query.all()
    for teeshirt in teeshirts:
        return {'teeshirts' : [teeshirt.to_dict() for teeshirt in teeshirts]}
        # return new_teeshirt.to_dict()

#Get a specific teeshirt 
@teeshirt_routes.route('/<int:id>', methods=['GET'])
def get_teeshirt(id):
    teeshirt = Teeshirt.query.get(id)
    return teeshirt.to_dict()

#Get all user teeshirts
@teeshirt_routes.route('/current', methods=['GET'])
def get_current_user_teeshirts():
    if current_user.is_authenticated:
        userId = current_user.id
        teeshirts = Teeshirt.query.filter(Teeshirt.user_id == userId).all()
        return {'teeshirts:': [teeshirt.to_dict() for teeshirt in teeshirts]}

#POST ROUTES

@teeshirt_routes.route('/<int:userId>/teeshirt/', methods=['POST'])
def create_a_teeshirt(userId):
    if current_user.is_authenticated:
        form = SellingForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        data = form.data
        teeshirt = Teeshirt(   
            name = data['name'],
            type = data['type'],
            description = data['description'],
            image_url = data['image_url'],
            brand = data['brand'],
            user_id = userId
        )
        db.session.add(teeshirt)
        db.session.commit()
        return teeshirt.to_dict()
        
#PUT ROUTES

@teeshirt_routes.route('/<int:id>/update', methods=['POST'])
def edit_teeshirt(id):
    if current_user.is_authenticated:
        form = SellingForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        data = form.data
        teeshirt_to_update = Teeshirt.query.get(id)
        if teeshirt_to_update.user_id == current_user.id:  # Update the line here
            teeshirt_to_update.name = data['name']  # Update the teeshirt_to_update object
            teeshirt_to_update.type = data['type']
            teeshirt_to_update.description = data['description']
            teeshirt_to_update.image_url = data['image_url']
            teeshirt_to_update.brand = data['brand']
            db.session.commit()
            print("PRINTS", teeshirt_to_update.to_dict())
            return teeshirt_to_update.to_dict()
        
        

#DELETE ROUTES

#Delete a teeshirt 
@teeshirt_routes.route('/delete/<int:id>', methods=['DELETE'])
def delete_teeshirt(id):
    if current_user.is_authenticated:
        teeshirt_to_delete = Teeshirt.query.get(id)
        if teeshirt_to_delete.user_id == current_user.id:
            db.session.delete(teeshirt_to_delete)
            db.session.commit()
            print("TEEGONE")
            return {'teeshirt': 'your teeshirt has been deleted'}
        else:
            return {'error': 'Unauthorized access'}
    else:
        return {'error': 'User not authenticated'}
