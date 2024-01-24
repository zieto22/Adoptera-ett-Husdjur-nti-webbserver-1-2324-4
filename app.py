from flask import Flask

from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  return '''
  
  <h1>Adopt a Pet!</h1>
  

  <p>Browse through the links below to find your n  kew furry friend</p>


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


@app.route('/animals/<pet_type>')
def animals(pet_type):

  for 
  
  
  return 'List of pet %s' % pet_type


app.run(debug=True, host="0.0.0.0")

#Remember remember to go back to number 7
#You are at number 11
