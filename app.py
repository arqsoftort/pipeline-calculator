#!flask/bin/python
from flask import Flask, jsonify
from random import randint
from uuid import uuid4

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'ok': True}), 200


@app.route('/pipeline-route/service/<service_point_id>', methods=['POST'])
def calculate_pipeline(service_point_id):
    sections = random_sections()
    return jsonify({'servicePointId': service_point_id, 'sections': sections}), 200


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'}), 405


def check_long(pipeline_id):
    errors = []

    if not pipeline_id:
        errors.append(error('Missing parameter', 'pipelineId'))
    elif not isinstance(pipeline_id, long):
        errors.append(error('Invalid parameter', 'pipelineId'))

    return errors


def random_sections():
    list = []
    for i in range(0, randint(1, 10)):
        list.append({
            'sourceId': uuid4(),
            'actuatorId': uuid4(),
            'sectionId': uuid4()
        })
    return list


def error(message, field=None):
    msg = {
        'message': message
    }
    if field:
        msg['field'] = field
    return msg


if __name__ == '__main__':
    app.run(debug=True)
