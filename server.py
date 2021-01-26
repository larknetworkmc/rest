import os
from eve import Eve
from eve.auth import BasicAuth

ADMIN_USERNAME    = os.environ['ADMIN_USERNAME']
ADMIN_PASSWORD    = os.environ['ADMIN_PASSWORD']

profile_schema = {
    'username': { 'type': 'string' },
    'uuid': { 'type': 'string' }
}

profiles = {
    'item_title': 'profile',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    'resource_methods': ['GET', 'POST'],
    'schema': profile_schema
}

domain = {
    'profiles': profiles
}

settings =  {
    'DOMAIN': domain,

    'MONGO_PORT': int(os.environ['MONGO_PORT']),
    'MONGO_HOST': os.environ['MONGO_HOST'],
    'MONGO_USERNAME': os.environ['MONGO_USERNAME'],
    'MONGO_PASSWORD': os.environ['MONGO_PASSWORD'],
    'MONGO_AUTH_SOURCE': os.environ['MONGO_AUTH_SOURCE'],
    'MONGO_DBNAME': os.environ['MONGO_DBNAME']
}

class RestAuth(BasicAuth):

    def check_auth(self, username, password, allowed_roles, resoruce, method):
        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

app = Eve(auth=RestAuth, settings=settings)

if __name__ == '__main__':
    app.run()
