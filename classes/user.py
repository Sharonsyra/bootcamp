from werkzeug.security import generate_password_hash


class User(object):
    """ Class user registers, signs in and has bucketlists and items """

    def __init__(self, username, email, password, bucketlists=[]):
        self.person_id = id(self)
        self.username = username
        self.email = email
        self.password = password
        self.bucketlists = bucketlists

    def __repr__(self):
        return "<User {}>".format(self.username)

    def hashed_password(self, new_password):
        """
        Hashes the new entered password
        """
        self.password = generate_password_hash(new_password)
