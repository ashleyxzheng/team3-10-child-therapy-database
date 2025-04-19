from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

children = Blueprint('children', __name__)

@children.route('/children', methods=['GET'])
def get_children():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Children')
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@children.route('/children', methods=['POST'])
def post_child():
    current_app.logger.info('POST /children route hit')

    new_child = request.json
    child_id = new_child['Child_ID']
    name = new_child['Name']
    age = new_child['Age']
    guardian = new_child['Guardian']

    insert_query = '''INSERT INTO Children
     (Child_ID, Name, Age, Guardian) VALUES 
     (%s, %s, %s, %s)'''
    
    data = (child_id, name, age, guardian)

    cursor = db.get_db().cursor()
    cursor.execute(insert_query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Child added", "id": child_id}), 201)

    return response

@children.route('/children/<id>', methods=['GET'])
def get_child(id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Children WHERE Child_ID = %s', (id,))
    theData = cursor.fetchone()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@children.route('/children/<id>', methods=['PUT'])
def update_child(id):
    current_app.logger.info('PUT /children/<id> route hit')

    updated_child = request.json
    name = updated_child['Name']
    age = updated_child['Age']
    guardian = updated_child['Guardian']

    update_query = '''UPDATE Children SET 
        Name = %s,
        Age = %s,
        Guardian = %s
        WHERE Child_ID = %s'''
    
    data = (name, age, guardian, id)

    cursor = db.get_db().cursor()
    cursor.execute(update_query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Child updated", "id": id}), 200)

    return response