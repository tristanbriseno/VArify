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

    query = '''
        query ($id: Int) { # Define which variables will be used in the query (id)
        Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
            id
            title {
            romaji
            english
            native
            }
        }
        }
        '''

    # Define our query variables and values that will be used in the query request
    variables = {
    'id': 15125
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})

    pp.pprint(response)
    context = {
        
        'id': variables['id']

    }



    return render_template('index.html', **context)

@app.route('/shows')
def shows():
    """returns a bunch of stuff"""
    return render_template('shows.html')





    


if __name__ == '__main__':
    app.run(debug=True)