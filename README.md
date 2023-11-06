# Install Requirements:

Create Environment:
python -m venv env

Activate:
env\Scripts\activate

Install requirements:
pip install -r requirements.txt

# Database Connection 
Set SQLALCHEMY_DATABASE_URI in Config.py and app/__init__.py

# Run the following commands in your terminal to create the SQLite database and the 'projects' table:

Commands : 
python
from app import db
db.create_all()
exit()

To start your Flask application, run:
python run.py
