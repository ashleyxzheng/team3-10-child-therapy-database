from flask import request, Blueprint, jsonify, make_response, current_app
from backend.db_connection import db

therapy_sessions = Blueprint('therapy_sessions', __name__)

"""
Therapy_Session does not exist yet
"""

@therapy_sessions.route('/therapy-sessions/<child_id>', methods=['GET'])
def get_sessions(child_id):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Therapy_Session WHERE Patient_ID = %s', (child_id,))
    return make_response(jsonify(cursor.fetchall()), 200)

@therapy_sessions.route('/therapy-sessions', methods=['POST'])
def post_session():
    data = request.json
    query = '''INSERT INTO Therapy_Session (Patient_ID, License_Number, Date, Notes)
               VALUES (%s, %s, %s, %s)'''
    values = (data['Patient_ID'], data['License_Number'], data['Date'], data['Notes'])
    cursor = db.get_db().cursor()
    cursor.execute(query, values)
    db.get_db().commit()
    return make_response(jsonify({'message': 'Session added'}), 201)
