from flask import Flask, render_template
import logic

MAIN_PAGE = 'home.html'


app = Flask(__name__)

@app.route('/')
def home():
  logic.example()
  return render_template(MAIN_PAGE)

if __name__ == '__main__':
  app.run(debug=True)
