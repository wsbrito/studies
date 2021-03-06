"""
REST application based on:
https://realpython.com/flask-connexion-rest-api/#using-connexion-to-add-a-rest-api-endpoint
"""
from flask import (Flask, render_template)
import connexion

# Create the application instance
# Para visualizar o swagger http://0.0.0.0:5000/api/ui
app = connexion.App(__name__, specification_dir="./")

# Read the swagger-original.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)