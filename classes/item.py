class Item(object):
    """ Class item belongs to a bucketlist """

    def __init__(self, name, done, date_created, date_modified):
        self.id = id(self)
        self.name = name
        self.done = done
        self.date_created = date_created
        self.date_modified = date_modified

    def __repr__(self):
        return "<Item {}>".format(self.name)
