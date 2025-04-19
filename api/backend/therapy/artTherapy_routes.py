from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

artTherapies = Blueprint('artTherapies', __name__)

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
    artType = new_art_therapy['Art_Type']
    medium = new_art_therapy['Medium']
    resource = new_art_therapy['Resources']
    benefits = new_art_therapy['Benefits']
    prompt = new_art_therapy['Prompt']

    insert_query = '''INSERT INTO Art_Therapy
     (Therapy_ID, Art_Type, Medium, Resources, Benefits, Prompt) VALUES 
     (%s, %s, %s, %s, %s, %s)'''
    
    data = (therapy_id, artType, medium, resource, benefits, prompt)

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
    artType = updated_art_therapy['Art_Type']
    medium = updated_art_therapy['Medium']
    resource = updated_art_therapy['Resources']
    benefits = updated_art_therapy['Benefits']
    prompt = updated_art_therapy['Prompt']

    query = '''UPDATE Art_Therapy SET 
        Art_Type = %s,
        Medium = %s,
        Resources = %s,
        Benefits = %s,
        Prompt = %s
        WHERE 
        Therapy_ID = %s
        '''
    
    data = (artType, medium, resource, benefits, prompt, artTherapyID)

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Art therapy updated", 
                                      "Therapy ID": artTherapyID}), 200)
    return response