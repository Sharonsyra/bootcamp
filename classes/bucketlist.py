class Bucketlist(object):
    """ Class Bucketlist belongs to a user """

    def __init__(self, name, date_created, date_modified, items=[]):
        self.id = id(self)
        self.name = name
        self.date_created = date_created
        self.date_modified = date_modified
        self.items = items

    def __repr__(self):
        return "<BucketList {}>".format(self.name)
