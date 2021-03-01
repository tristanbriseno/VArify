import requests 

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

# Define our query variables and values that will be used in the query request
variables = {
    'name': 'Michael Tatum'
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})

print(response.text)