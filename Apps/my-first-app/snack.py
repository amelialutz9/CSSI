from google.appengine.ext import ndb

# Kind (string)
# Rating (int)
# Quantity (int)
# Calories (int)
# Expiration (date)

# make a request to /snack?name=Chips&quantity=10 to
# add a new Snack to the datastore


class Snack(ndb.Model):
    kind = ndb.StringProperty()
    rating = ndb.IntegerProperty()
    quantity = ndb.IntegerProperty()
    calories = ndb.IntegerProperty()
    #expiration = ndb.DateProperty()
