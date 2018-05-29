from ..app import db
from ..model import User,Record,Picture,Job,Resource
db.create_all()
print("created")