class User(object):
    """ Class user registers, signs in and has bucketlists and items """

    def __init__(self, username, email, password, bucketlists=[]):
        self.person_id = id(self)
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User {}>".format(self.username)
