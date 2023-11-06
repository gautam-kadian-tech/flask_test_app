# Install Requirements:

pip install flask sqlalchemy flask-restful

# Run the following commands in your terminal to create the SQLite database and the 'projects' table:

Commands : 
python
from app import db
db.create_all()
exit()

To start your Flask application, run:
python run.py