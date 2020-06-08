import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow

from pprint import pprint

import json

d_contacts={
    'resourceName':'',
    'etag':'',
    'names':[{
        'displayName':'',
        'displayNameLastFirst':'',
        'givenName':'',
        'metadata':{
            'primary':'',
            'source':{
                'id':'',
                'type':''
            }
        }
    }]
}

def get_contacts():
  dd_contacts={}
  # Set up a Flow object to be used if we need to authenticate. This
  # sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
  # the information it needs to authenticate. Note that it is called
  # the Web Server Flow, but it can also handle the flow for
  # installed applications.
  #
  # Go to the Google API Console, open your application's
  # credentials page, and copy the client ID and client secret.
  # Then paste them into the following code.
  FLOW = OAuth2WebServerFlow(
      client_id='720357279015-91d4k7h3osnckgbp8e1gn3l4e1u8319p.apps.googleusercontent.com',
      client_secret='4tGp20usVPn8lajJLshE7RaL',
      scope='https://www.googleapis.com/auth/contacts.readonly',
      user_agent='test_python_people_api')

  # If the Credentials don't exist or are invalid, run through the
  # installed application flow. The Storage object will ensure that,
  # if successful, the good Credentials will get written back to a
  # file.
  storage = Storage('info.dat')
  credentials = storage.get()
  if credentials is None or credentials.invalid == True:
    credentials = run_flow(FLOW, storage)

  # Create an httplib2.Http object to handle our HTTP requests and
  # authorize it with our good Credentials.
  http = httplib2.Http()
  http = credentials.authorize(http)

  # Build a service object for interacting with the API. To get an API key for
  # your application, visit the Google API Console
  # and look at your application's credentials page.
  people_service = build(serviceName='people', version='v1', http=http)
  connections = people_service.people().connections().list(resourceName='people/me', personFields='names,emailAddresses')

  all_connections = connections.execute()['connections']
  number_of_connections = len(all_connections)

  for i in range(0,number_of_connections):
    # print all_connections[i]
    _resourceName = all_connections[i]['resourceName']
    dd_contacts[_resourceName]=all_connections[i]

  return dd_contacts



def main():
  dd_contacts = get_contacts()
  pprint(dd_contacts)
  pass

if __name__ == '__main__':
  main()
