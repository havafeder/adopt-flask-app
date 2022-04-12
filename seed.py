from app import db
from models import Pet

db.drop_all()
db.create_all()

pet = Pet(name="Bubbles", species="Dog", photo_url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thepioneerwoman.com%2Fhome-lifestyle%2Fpets%2Fg33851902%2Fsmall-dog-breeds%2F&psig=AOvVaw11-vw7CYcVw37wOi7ru42O&ust=1649828065417000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCNi7n9DmjfcCFQAAAAAdAAAAABAE",
			age=5, notes="Patient and loves food.", available=True)
			
db.session.add(pet)
db.session.commit()