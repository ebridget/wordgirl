# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
import logic

MAIN_PAGE = 'home.html'


# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
  logic.example()
  return render_template(MAIN_PAGE)

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['url']
    email=request.form['keyword']
    return render_template('form_action.html', name=name, email=email)
"""
# Run the app :)
if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("5000")
  )
"""
if __name__ == '__main__':
    app.run(debug=True)
