from flask import Flask, render_template, redirect, jsonify, flash, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def list_pets():
	"""List pets"""

	pets = Pet.query.all()
	render_template("listings.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
	"""Add pet"""

	form = AddPetForm()

	if form.validate_on_submit():
		data = {k: v for k, v in form.data.items() if k != "csrf_token"}
		new_pet = Pet(**data)
		db.session.add(new_pet)
		db.session.commit()
		flash(f"{new_pet.name} added.")
		return redirect(url_for('list_pets'))
	else:
		return render_template("add_pet_form.html", form=form)

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)