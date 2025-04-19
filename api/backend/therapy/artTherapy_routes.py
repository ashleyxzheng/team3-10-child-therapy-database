from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

artTherapies = Blueprint('artTherapy', __name__)

@artTherapies.route('/art-therapies', methods=['GET'])
def get_art_therapies():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Art_Therapy')
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@artTherapies.route('/art-therapies', methods=['POST'])
def post_art_therapy():
    current_app.logger.info('POST /art-therapies route hit')

    new_art_therapy = request.json
    therapy_id = new_art_therapy['Therapy_ID']
    name = new_art_therapy['Name']
    description = new_art_therapy['Description']

    insert_query = '''INSERT INTO Art_Therapy
     (Therapy_ID, Name, Description) VALUES 
     (%s, %s, %s)'''
    
    data = (therapy_id, name, description)

    cursor = db.get_db().cursor()
    cursor.execute(insert_query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Art therapy added", "id": therapy_id}), 201)

    return response

@artTherapies.route('/art-therapies/<int:artTherapyID>', methods=['GET'])
def get_art_therapy(artTherapyID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Art_Therapy WHERE Therapy_ID = %s', (artTherapyID,))
    theData = cursor.fetchone()
    if not theData:
        return make_response(jsonify({"error": "Art therapy not found"}), 404)
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@artTherapies.route('/art-therapies/<int:artTherapyID>', methods=['PUT'])
def update_art_therapy(artTherapyID):
    current_app.logger.info('PUT /art-therapies route hit')

    updated_art_therapy = request.json
    name = updated_art_therapy['Name']
    description = updated_art_therapy['Description']

    query = '''UPDATE Art_Therapy SET 
        Name = %s,
        Description = %s
        WHERE 
        Therapy_ID = %s
        '''
    
    data = (name, description, artTherapyID)

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Art therapy updated", 
                                      "Therapy ID": artTherapyID}), 200)
    return response