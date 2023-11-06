from flask import request
from flask_restful import Resource, Api
from app import app, db
from app.models import Project

api = Api(app)

class ProjectResource(Resource):
    def get(self, id=None):
        if id is None:
            """Get Projects List"""
            projects = Project.query.all()
            project_list = [
                {
                    'id': project.id,
                    'title': project.title,
                    'description': project.description,
                    'completed': project.completed,
                    'created_at': project.formatted_created_at
                }
                for project in projects
            ]
            return project_list
        else:
            """Get Project By ID"""
            project = Project.query.get(id)
            if project is None:
                return {'error': 'Project not found'}, 404

            project_info = {
                'id': project.id,
                'title': project.title,
                'description': project.description,
                'completed': project.completed,
                'created_at': project.formatted_created_at
            }
            return project_info

    def post(self):
        """Create New Project"""
        data = request.get_json()
        if not data or 'title' not in data:
            return {'error': 'Title is required'}, 400
        project = Project(title=data['title'], description=data.get('description', ''), completed=data.get('completed', False))
        db.session.add(project)
        db.session.commit()
        return {'message': 'Project created successfully'}, 201

    def put(self, id):
        """Update Project By ID"""
        project = Project.query.get(id)
        if project is None:
            return {'error': 'Project not found'}, 404
        data = request.get_json()
        if not data:
            return {'error': 'No data provided for update'}, 400
        if 'title' in data:
            project.title = data['title']
        if 'description' in data:
            project.description = data['description']
        if 'completed' in data:
            project.completed = data['completed']
        db.session.commit()
        return {'message': 'Project updated successfully'}

    def delete(self, id):
        """Delete Project By ID"""
        project = Project.query.get(id)
        if project is None:
            return {'error': 'Project not found'}, 404
        db.session.delete(project)
        db.session.commit()
        return {'message': 'Project deleted successfully'}

api.add_resource(ProjectResource, '/projects', '/projects/<int:id>')
