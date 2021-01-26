import os

MONGO_PORT        = int(os.environ['MONGO_PORT'])
MONGO_HOST        = os.environ['MONGO_HOST']
MONGO_USERNAME    = os.environ['MONGO_USERNAME']
MONGO_PASSWORD    = os.environ['MONGO_PASSWORD']
MONGO_AUTH_SOURCE = os.environ['MONGO_AUTH_SOURCE']
MONGO_DBNAME      = os.environ['MONGO_DBNAME']

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

DOMAIN = {
    'profiles': profiles
}
