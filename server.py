from eve import Eve
from eve.auth import BasicAuth
from settings import ADMIN_PASSWORD, ADMIN_USERNAME

class RestAuth(BasicAuth):

    def check_auth(self, username, password, allowed_roles, resoruce, method):
        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

app = Eve(auth=RestAuth)

if __name__ == '__main__':
    app.run()
