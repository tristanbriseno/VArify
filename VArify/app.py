import jinja2
from flask import Flask, request, redirect, render_template, url_for
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
from pprint import PrettyPrinter
import os
import requests
import json

app = Flask(__name__, template_folder="templates")

load_dotenv()
API_KEY = os.getenv('API_KEY')
pp = PrettyPrinter(indent=4)


@app.route('/')
def page():
    """Display the web page."""

    full_name = request.args.get('full-name')
    character_list = []


    query = '''
    query ($name: String) {
        Staff(search: $name) {
            id
            characters{
                nodes {
                    id
                    name {
                        full
            }
            }
            }
        }
        }
        '''
    variables = {
    'name': full_name
        }

    url = 'https://graphql.anilist.co'

    
    result_json = requests.post(url, json={'query': query, 'variables': variables})
    json_response = json.loads(result_json.text)
    

    for i in range(len(json_response["data"]["Staff"]["characters"]["nodes"])):
        character_list.append(json_response["data"]["Staff"]["characters"]["nodes"][i]["name"])
    
    

    # while json_response["data"]["Staff"]["characters"]["nodes"][i] != None:
    #     print(i["name"])
    
    
    context = {
        'full_name': full_name,
        "character_list": character_list
        
       
    }
    return render_template('index.html', **context)

@app.route('/shows')
def shows():
    """returns a bunch of stuff"""
    return render_template('shows.html')





    


if __name__ == '__main__':
    app.run(debug=True)