from flask import Flask

from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  return '''
    <h1>Adopt a Pet!</h1>

    <p>Browse through the links below to find your new furry friend</p>

    <ul>
        <li>
            <a href="/animals/Dogs">
                Dogs
            </a>
        </li>

        <li>
            <a href="/animals/Cats">
                Cats
            </a>
        </li>

        <li>
            <a href="/animals/Rabbits">
                Rabbits
            </a>
        </li>    
    </ul>
    '''


@app.route('/animals/<string:pet_type>')
def animals(pet_type):
  html = f"<h1>List of {pet_type.capitalize()}</h1>"

  html += "<ul>"
  for pet_id, pet in enumerate(pets[pet_type.lower()], start=1):
    html += f"<li><a href='/animals/{pet_type.lower()}/{pet_id}'>{pet['name']}</a></li>"
  html += "</ul>"

  return html


@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet_list = pets.get(pet_type.lower())

  if pet_list is None or pet_id < 1 or pet_id > len(pet_list):
    return f'invalid pet id {pet_id}'

  pet = pet_list[pet_id - 1]

  pet_name = pet['name']

  return f'''
  <h1>{pet_name}</h1>
  <p>Age: {pet['age']}</p>
  <p>Breed: {pet['breed']}</p>
  <p>desciprtion: {pet['description']}</p>
  <img src="{pet['url']}" alt="{pet['name']}">
  '''


#Done

app.run(debug=True, host="0.0.0.0")
