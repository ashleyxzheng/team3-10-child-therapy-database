from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

children = Blueprint('children', __name__)

@children.route('/children', methods=['GET'])
def get_children():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Child')
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

@children.route('/children', methods=['POST'])
def post_child():
    current_app.logger.info('POST /children route hit')

    new_child = request.json
    child_id = new_child['Patient_ID']
    name = new_child['Name']
    age = new_child['Age']
    gender = new_child['Gender']
    preferredArt = new_child['Preferred_Art']
    chronicCondition = new_child['Chronic_Condition']
    personalityTraits = new_child['Personality_Traits']
    contextAwareReplies = new_child['Context_Aware_Replies']
    personalInfo = new_child['Personal_Info']

    insert_query = '''INSERT INTO Child
     (Patient_ID, Name, Age, Gender, Preferred_Art, 
     Chronic_Condition, Personality_Traits, Context_Aware_Replies, Personal_Info) VALUES 
     (%s, %s, %s, %s, %s, %s, %s, %s)'''
    
    data = (child_id, name, age, gender, preferredArt, 
            chronicCondition, personalityTraits, contextAwareReplies, personalInfo)

    cursor = db.get_db().cursor()
    cursor.execute(insert_query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Child added", "id": child_id}), 201)

    return response

@children.route('/children/<id>', methods=['GET'])
def get_child(id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Child WHERE Child_ID = %s', (id,))
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
    gender = updated_child['Gender']
    preferredArt = updated_child['Preferred_Art']
    chronicCondition = updated_child['Chronic_Condition']
    personalityTraits = updated_child['Personality_Traits']
    contextAwareReplies = updated_child['Context_Aware_Replies']
    personalInfo = updated_child['Personal_Info']

    update_query = '''UPDATE Child SET 
        Name = %s,
        Age = %s,
        Gender = %s,
        Preferred_Art = %s,
        Chronic_Condition = %s,
        Personality_Traits = %s,
        Context_Aware_Replies = %s,
        Personal_Info = %s
        WHERE Child_ID = %s'''
    
    data = (name, age, gender, preferredArt, chronicCondition, personalityTraits, contextAwareReplies, personalInfo, id)

    cursor = db.get_db().cursor()
    cursor.execute(update_query, data)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Child updated", "id": id}), 200)

    return response

@children.route('/children/<id>', methods=['DELETE'])
def delete_child(id):
    current_app.logger.info('DELETE /children/<id> route hit')

    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM Child WHERE Child_ID = %s', (id,))
    db.get_db().commit()
    response = make_response(jsonify({"message": "Child deleted", "id": id}), 200)

    return response