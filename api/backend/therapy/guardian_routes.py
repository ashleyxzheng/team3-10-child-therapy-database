from flask import request
from flask import Blueprint
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

guardians = Blueprint('guardians', __name__)

@guardians.route('/guardians', methods=['GET'])
def get_guardians():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM Guardian''')
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@guardians.route('/guardians', methods=['POST'])
def post_guardians():
    current_app.logger.info('POST /guardians route hit')

    new_guardian = request.json
    guardianID = new_guardian['Guardian_ID']
    name = new_guardian['Name']
    email = new_guardian['Email']
    phone = new_guardian['Phone']
    relationship = new_guardian['Relationship']
    personalInfo = new_guardian['Personal_Info']

    insert_query = '''INSERT INTO Guardian 
    (Guardian_ID, Name, Email, Phone, Relationship, Personal_Info VALUES
    (%s, %s, %s, %s, %s, %s)'''

    data = (guardianID, name, email, phone, relationship, personalInfo)

    cursor = db.get_db().cursor()
    cursor.execute(insert_query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message" : "Guardian added", "id" : guardianID}), 201)
    return response

@guardians.route('/guardians/<gID>', methods=['GET'])
def get_guardian(gID):
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM Guardian WHERE Guardian_ID = %s,)''', (gID,))
    theData = cursor.fetchone()

    the_response = make_response(theData, 200)
    return the_response

@guardians.route('/guardians/<guardianID>', methods=['PUT'])
def update_guardian(guardianID):
    cursor = db.get_db().cursor()
    new_g = request.json
    name = new_g['Name']
    email = new_g['Email']
    phone = new_g['Phone']
    relationship = new_g['Relationship']
    personalInfo = new_g['Personal_Info']

    query = '''UPDATE Guardian SET 
        Name = %s,
        Email = %s,
        Phone = %s,
        Relationship = %s,
        Personal_Info = %s
        WHERE
        Guardian_ID = %s
    '''

    data = (name, email, phone, relationship, personalInfo, guardianID)
    
    cursor.execute(query, data)
    db.get_db().commit()
    response = make_response(jsonify({"Message" : "guardian updated", 
                                      "Guardian ID" : guardianID}), 200)
    return response


