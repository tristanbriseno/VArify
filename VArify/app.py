import jinja2
from flask import Flask, request, redirect, render_template, url_for
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
from pprint import PrettyPrinter
import os

app = Flask(__name__, template_folder="templates")

load_dotenv()
API_KEY = os.getenv('API_KEY')
pp = PrettyPrinter(indent=4)


@app.route('/')
def page():
    """Display the web page."""
    va_search = request.args.get('name-query')
    print(va_search)


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)