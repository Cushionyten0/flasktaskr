from project import db
from project.models import User, Task
from datetime import date

# create the database an the db table
db.create_all()  # eventually calls db.Model.metadata.create_all

# insert data
db.session.add(User("admin", "ad@min.com", "admin", "admin"))
db.session.add(Task("Finish this tutorial", date(2015, 3, 13), 10,
                    date(2015, 3, 13), 1, 1))
db.session.add(Task("Finish Real Python", date(2015, 3, 13), 10,
                    date(2015, 3, 13), 1, 1))

# commit the changes
db.session.commit()
