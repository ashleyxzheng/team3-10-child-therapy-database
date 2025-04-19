from flask import request, Blueprint, jsonify, make_response, current_app
from backend.db_connection import db

assignments = Blueprint('assignments', __name__)

# child and therapist pairs

@assignments.route('/assignments/child-therapist', methods=['GET'])
def get_therapy_pairs():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Provides_Treatment')
    return make_response(jsonify(cursor.fetchall()), 200)

@assignments.route('/assignments/child-therapist', methods=['POST'])
def assign_therapist():
    data = request.json
    query = 'INSERT INTO Provides_Treatment (License_Number, Therapy_ID) VALUES (%s, %s)'
    values = (data['License_Number'], data['Therapy_ID'])
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    return make_response(jsonify({'message': 'Assignment added'}), 201)

@assignments.route('/assignments/child-therapist', methods=['DELETE'])
def unassign_therapist():
    data = request.json
    query = 'DELETE FROM Provides_Treatment WHERE License_Number = %s AND Therapy_ID = %s'
    values = (data['License_Number'], data['Therapy_ID'])
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    return make_response(jsonify({'message': 'Assignment removed'}), 200)

# therapist and supervisor pairs

@assignments.route('/assignments/supervisor-therapist', methods=['GET'])
def get_supervisor_pairs():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Monitors')
    return make_response(jsonify(cursor.fetchall()), 200)

@assignments.route('/assignments/supervisor-therapist', methods=['POST'])
def assign_supervisor():
    data = request.json
    query = '''INSERT INTO Monitors (Supervisor_ID, License_Number, Start_Date, End_Date, Feedback)
               VALUES (%s, %s, %s, %s, %s)'''
    values = (data['Supervisor_ID'], data['License_Number'], data['Start_Date'], data['End_Date'], data['Feedback'])
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    return make_response(jsonify({'message': 'Supervisor assigned'}), 201)
