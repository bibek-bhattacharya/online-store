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


#SQL - Initial state
# INSERT INTO products (name, price)
# VALUES
# ('Lavender heart', '9.25'),
# ('Personalised cufflinks', '45.00'),
# ('Kids T-shirt', '19.95');

# select * from products;