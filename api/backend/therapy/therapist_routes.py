from flask import request
from flask import Blueprint
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

therapists = Blueprint('therapists', __name__)

@therapists.route('/therapists', methods=['GET'])
def get_therapists():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM Therapist''')
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@therapists.route('/therapists', methods=['POST'])
def post_therapists():
    current_app.logger.info('POST /therapists route hit')
    new_sup = request.json
    licenseNumber = new_sup['License_Number']
    name = new_sup['Name']
    email = new_sup['Email']
    phone = new_sup['Phone']
    age = new_sup['Age']
    gender = new_sup['Gender']
    personalInfo = new_sup['Personal_Info']
    preferredArtForm = new_sup['Preferred_Art_Form']
    techniqueConfidence = new_sup['Technique_Confidence']
    specialization = new_sup['Specialization']

    insert_query = '''INSERT INTO Training_Supervisor
     (License_Number, Name, Email, Phone, Age, Gender, 
     Personal_Info, Preferred_Art_Form, Technique_Confidence, 
     Specialization) VALUES 
     (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    
    data = (licenseNumber, 
            name, 
            email, 
            phone, 
            age, 
            gender, 
            personalInfo, 
            preferredArtForm, 
            techniqueConfidence, 
            specialization)

    cursor = db.get_db().cursor()
    r = cursor.execute(insert_query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Therapist added", "id": licenseNumber}), 201)

    return response

@therapists.route('/therapists/<userID>', methods=['GET'])
def get_therapist(userID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Therapist WHERE License_Number = %s', (userID,))

    theData = cursor.fetchone()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200

    return the_response

@therapists.route('/therapists/<userID>', methods=['PUT'])
def update_therapist(userID):
    current_app.logger.info('PUT /therapist route')

    new_therapist = request.json
    name = new_therapist['Name']
    email = new_therapist['Email']
    phone = new_therapist['Phone']
    age = new_therapist['Age']
    gender = new_therapist['Gender']
    personalInfo = new_therapist['Personal_Info']
    preferredArtForm = new_therapist['Preferred_Art_Form']
    techniqueConfidence = new_therapist['Technique_Confidence']
    specialization = new_therapist['Specialization']

    query = '''UPDATE Therapist SET
        name = %s
        email = %s
        phone = %s
        age = %s
        gender = %s
        personalInfo = %s
        preferredArtForm = %s
        techniqueConfidence = %s
        specialization = %s
        WHERE
        LicenseNumber = %s
        '''
    
    data = (name, email, phone, age, gender, personalInfo, preferredArtForm, techniqueConfidence, specialization)

    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    response = make_response(jsonify({"Message" : "Therapist updated", "TherapistLicense" : userID}),200)
    return response

@therapists.route('/therapists/<userID>', methods=['DELETE'])
def delete_therapist(userID):
    current_app.logger.info('DELETE /therapist route')

    cursor = db.get_db().cursor()
    cursor.execute('''DELETE FROM Therapist WHERE License_Number = %s''', (userID,))
    db.get_db().commit()
    response = make_response(jsonify({"Message" : "Deleted", "licenseID" : userID}))
    return response


