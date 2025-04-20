from flask import request, Blueprint, jsonify, make_response, current_app
from backend.db_connection import db

specialists = Blueprint('specialists', __name__)

@specialists.route('/specialists', methods=['GET'])
def get_specialists():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM Art_Therapy_Specialist''')
    theData = cursor.fetchall()
    response = make_response(jsonify(theData), 200)
    return response

@specialists.route('/specialists', methods=['POST'])
def post_specialist():
    current_app.logger.info('POST /specialists route hit')
    new_specialist = request.json

    specialistID = new_specialist['Specialist_ID']
    name = new_specialist['Name']
    email = new_specialist['Email']
    phone = new_specialist['Phone']
    expertise = new_specialist['Art_Specialization']
    bio = new_specialist['Bio']

    insert_query = '''
        INSERT INTO Art_Therapy_Specialist 
        (Specialist_ID, Name, Email, Phone, Art_Specialization, Bio)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    data = (specialistID, name, email, phone, expertise, bio)

    cursor = db.get_db().cursor()
    cursor.execute(insert_query, data)
    db.get_db().commit()

    return make_response(jsonify({"message": "Specialist added", "id": specialistID}), 201)

@specialists.route('/specialists/<int:specialistID>', methods=['GET'])
def get_specialist(specialistID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Art_Therapy_Specialist WHERE Specialist_ID = %s', (specialistID,))
    data = cursor.fetchone()

    if not data:
        return make_response(jsonify({"error": "Specialist not found"}), 404)

    return make_response(jsonify(data), 200)

@specialists.route('/specialists/<int:specialistID>', methods=['PUT'])
def update_specialist(specialistID):
    updated_specialist = request.json

    name = updated_specialist['Name']
    email = updated_specialist['Email']
    phone = updated_specialist['Phone']
    expertise = updated_specialist['Art_Specialization']
    bio = updated_specialist['Bio']

    query = '''
        UPDATE Art_Therapy_Specialist SET 
        Name = %s,
        Email = %s,
        Phone = %s,
        Art_Specialization = %s,
        Bio = %s
        WHERE Specialist_ID = %s
    '''
    data = (name, email, phone, expertise, bio, specialistID)

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    return make_response(jsonify({"message": "Specialist updated", "Specialist ID": specialistID}), 200)