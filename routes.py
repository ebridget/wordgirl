# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
import logic, parser

MAIN_PAGE = 'home.html'


# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
  return render_template(MAIN_PAGE)

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/submitform/', methods=['POST'])

def submitform():
    url=request.form['url']
    keyword=request.form['keyword']
    text=parser.extract(url)
    word_list,percentage=logic.similar_words(keyword, text)
    return render_template('results.html',similarwords=word_list,percentage=percent)

@app.route('/searchagain/', methods=['POST'])
def searchagain():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
