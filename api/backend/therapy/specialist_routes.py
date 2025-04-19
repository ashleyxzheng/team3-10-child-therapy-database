from flask import request, Blueprint, jsonify, make_response, current_app
from backend.db_connection import db

specialists = Blueprint('specialists', __name__)

@specialists.route('/specialists', methods=['GET'])
def get_specialists():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM Specialist''')
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@specialists.route('/specialists', methods=['POST'])
def post_specialists():
    current_app.logger.info('POST /specialists route hit')

    new_specialist = request.json
    specialistID = new_specialist['Specialist_ID']
    name = new_specialist['Name']
    email = new_specialist['Email']
    phone = new_specialist['Phone']
    expertise = new_specialist['Expertise']
    bio = new_specialist['Bio']

    insert_query = '''INSERT INTO Specialist 
    (Specialist_ID, Name, Email, Phone, Expertise, Bio) VALUES
    (%s, %s, %s, %s, %s, %s)'''

    data = (specialistID, name, email, phone, expertise, bio)

    cursor = db.get_db().cursor()
    cursor.execute(insert_query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Specialist added", "id": specialistID}), 201)
    return response

@specialists.route('/specialists/<specialistID>', methods=['GET'])
def get_specialist(specialistID):
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM Specialist WHERE Specialist_ID = %s''', (specialistID,))
    theData = cursor.fetchone()

    if not theData:
        return make_response(jsonify({"error": "Specialist not found"}), 404)

    the_response = make_response(jsonify(theData), 200)
    return the_response

@specialists.route('/specialists/<specialistID>', methods=['PUT'])
def update_specialist(specialistID):
    cursor = db.get_db().cursor()
    updated_specialist = request.json
    name = updated_specialist['Name']
    email = updated_specialist['Email']
    phone = updated_specialist['Phone']
    expertise = updated_specialist['Expertise']
    bio = updated_specialist['Bio']

    query = '''UPDATE Specialist SET 
        Name = %s,
        Email = %s,
        Phone = %s,
        Expertise = %s,
        Bio = %s
        WHERE
        Specialist_ID = %s
    '''

    data = (name, email, phone, expertise, bio, specialistID)
    
    cursor.execute(query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Specialist updated", 
                                      "Specialist ID": specialistID}), 200)
    return response