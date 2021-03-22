import flask
from flask import jsonify, request
from . import db_session
from .jobs import Jobs
from datetime import datetime


blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict() for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobsId>', methods=['GET'])
def get_one_jobs(jobsId):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobsId)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify({'jobs': jobs.to_dict()})


@blueprint.route('/api/jobs/<int:jobsId>', methods=['DELETE'])
def delete_one_jobs(jobsId):
    try:
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).get(jobsId)
        db_sess.delete(jobs)
        db_sess.commit()
        return jsonify({'success': 'OK'})
    except Exception as e:
        return jsonify({'error': 'Not found'})


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Keys must be: id, team_leader, job, work_size, collaborators, is_finished'})
    db_sess = db_session.create_session()

    try:
        info = {
            "id": request.json['id'],
            "team_leader": request.json['team_leader'],
            "job": request.json['job'],
            "work_size": request.json['work_size'],
            "collaborators": request.json['collaborators'],
            "is_finished": request.json['is_finished']
        }
    except Exception as e:
        return jsonify({'error': 'Bad values: id=Integer, team_leader=Integer, job=String, work_size=Integer, collaborators=String, is_finished=Bool'})

    try:
        if "start_date" in request.json:
            info["start_date"] = datetime.strptime(
                request.json["start_date"], '%Y:%m:%d %h:%m:%s')
    except Exception as e:
        return jsonify({'error': 'Bad date format. Must be "%Y:%m:%d %h:%m:%s"'})
    try:
        if "end_date" in request.json:
            info["end_date"] = datetime.strptime(
                request.json["end_date"], '%Y:%m:%d %h:%m:%s')
    except Exception as e:
        return jsonify({'error': 'Bad date format. Must be "%Y:%m:%d %h:%m:%s"'})

    jobs = Jobs(**info)
    db_sess.add(jobs)
    try:
        db_sess.commit()
    except Exception as e:
        return jsonify({'error': 'Id already exists'})

    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobsId>', methods=['PUT'])
def edit_jobs(jobsId):
    if not request.json:
        return jsonify({'error': 'Empty request'})

    try:
        if "start_date" in request.json:
            request["start_date"] = datetime.strptime(
                request.json["start_date"], '%Y:%m:%d %h:%m:%s')
    except Exception as e:
        return jsonify({'error': 'Bad date format. Must be "%Y:%m:%d %h:%m:%s"'})
    try:
        if "end_date" in request.json:
            request["end_date"] = datetime.strptime(
                request.json["end_date"], '%Y:%m:%d %h:%m:%s')
    except Exception as e:
        return jsonify({'error': 'Bad date format. Must be "%Y:%m:%d %h:%m:%s"'})

    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobsId)
    try:
        for key in request.json:
            if key in dir(jobs):
                setattr(jobs, key, request.json[key])
        db_sess.commit()
    except Exception as e:
        return jsonify({'error': 'Bad format.'})

    return jsonify({'success': 'OK'})
