import jinja2
from flask import Flask, request, redirect, render_template, url_for
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
from pprint import PrettyPrinter
import os
import requests

app = Flask(__name__, template_folder="templates")

load_dotenv()
API_KEY = os.getenv('API_KEY')
pp = PrettyPrinter(indent=4)


@app.route('/')
def page():
    """Display the web page."""

    #Getting the first and last name of a character in an anime for use in our API call. 
    first_name = request.args.get('first-name-query')
    last_name = request.args.get('last-name-query')

    url = 'https://private-2139da-animedb.apiary-mock.com/api/characters'

    # # params = {

    # #     # 'app_id': '8f2c6d67',
    # #     # 'app_key': 'e5e5bdc2fdb7f36e504cc8478d9f88fe',
    # #      'first_name': first_name
    # #     # 'last_name': last_name

    # # }

    # result_json = requests.get(url).json()
    # # pp.pprint(result_json)
    context = {
        # 'description': result_json[0]['description'],
        'first_name': first_name,
        'last_name':last_name
        


    }

    return render_template('index.html', **context)

@app.route('/shows')
def shows():
    """returns a bunch of stuff"""
    return render_template('shows.html')





    


if __name__ == '__main__':
    app.run(debug=True)