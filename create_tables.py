#Create Database Tables
#python
from app.models.shared import db
from app import create_app
app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()
ctx.pop()
exit()