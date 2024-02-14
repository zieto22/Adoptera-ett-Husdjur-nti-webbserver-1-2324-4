"""A Flask application for adopting pets.

This application allows users to browse and adopt pets of different types, such as dogs, cats, and rabbits.

Routes:
- `/`: The root URL that displays links to browse different types of pets.
- `/animals/<pet_type>`: URL that displays a list of pets of the specified type.
- `/animals/<pet_type>/<pet_id>`: URL that displays the details of a specific pet.

Modules:
- `helper`: A module that provides a dictionary of pets categorized by type.

"""

from flask import Flask
from helper import pets

app = Flask(__name__)

# ... rest of the code ...
"""_summary_

  Returns:
      _type_: _description_
  """

from flask import Flask

from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  """
  Handles GET requests for the root URL.

  Returns:
    str: HTML content for the index page.
  """
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
  """
  Handles GET requests for the '/animals/<pet_type>' URL.

  Args:
    pet_type (str): The type of pet.

  Returns:
    str: HTML content for the list of pets of the specified type.
  """
  html = f"<h1>List of {pet_type.capitalize()}</h1>"

  html += "<ul>"
  for pet_id, pet in enumerate(pets[pet_type.lower()], start=1):
    html += f"<li><a href='/animals/{pet_type.lower()}/{pet_id}'>{pet['name']}</a></li>"
  html += "</ul>"

  return html


@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  """
  Handles GET requests for the '/animals/<pet_type>/<pet_id>' URL.

  Args:
    pet_type (str): The type of pet.
    pet_id (int): The ID of the pet.

  Returns:
    str: HTML content for the details of the specified pet.
  """
  pet_list = pets.get(pet_type.lower())

  if pet_list is None or pet_id < 1 or pet_id > len(pet_list):
    return f'invalid pet id {pet_id}'

  pet = pet_list[pet_id - 1]

  pet_name = pet['name']

  return f'''
  <h1>{pet_name}</h1>
  <p>Age: {pet['age']}</p>
  <p>Breed: {pet['breed']}</p>
  <p>Description: {pet['description']}</p>
  <img src="{pet['url']}" alt="{pet['name']}">
  '''


app.run(debug=True, host="0.0.0.0")
