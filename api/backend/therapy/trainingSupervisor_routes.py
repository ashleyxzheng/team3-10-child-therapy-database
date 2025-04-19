from flask import request
from flask import Blueprint
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

supervisors = Blueprint('supervisors', __name__)

@supervisors.route('/training-supervisors', methods=['GET'])
def get_supervisors():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT * FROM Training_Supervisor''')
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@supervisors.route('/training-supervisors', methods=['POST'])
def post_supervisors():
    current_app.logger.info('POST /supervisors route hit')

    new_sup = request.json
    sup_id = new_sup['Supervisor_ID']
    name = new_sup['Name']
    email = new_sup['Email']
    phone = new_sup['Phone']
    personalInfo = new_sup['Personal_Info']

    insert_query = '''INSERT INTO Training_Supervisor
     (Supervisor_ID, Name, Email, Phone, Personal_Info) VALUES 
     (%s, %s, %s, %s, %s)'''
    
    data = (sup_id, name, email, phone, personalInfo)

    cursor = db.get_db().cursor()
    r = cursor.execute(insert_query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Supervisor added", "id": sup_id}), 201)

    return response

@supervisors.route('/training-supervisors/<userID>', methods=['GET'])
def get_supervisor(userID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Training_Supervisor WHERE Supervisor_ID = %s', (userID,))

    theData = cursor.fetchone()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@supervisors.route('/training-supervisors/<userID>', methods=['PUT'])
def update_supervisor(userID):
    current_app.logger.info('PUT /supervisor route')
    
    new_sup = request.json
    sup_id = new_sup['Supervisor_ID']
    name = new_sup['Name']
    email = new_sup['Email']
    phone = new_sup['Phone']
    personalInfo = new_sup['Personal_Info']

    query = '''UPDATE Training_Supervisor SET 
        name = %s,
        email = %s,
        phone = %s,
        personalInfo = %s
        WHERE 
        Supervisor_ID = %s
        '''
    
    data = (name, email, phone, personalInfo, userID)

    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    response = make_response(jsonify({"Message" : "supervisor updated", 
                                      "Supervisor ID" : userID}), 200)
    return response