from google.appengine.ext import ndb
from random import randint

class FacebookPost(ndb.Model):
    name = ndb.StringProperty()
    text_content = ndb.StringProperty()
    num_likes = ndb.IntegerProperty()
    num_happy_reax = ndb.IntegerProperty()
    num_sad_reax = ndb.IntegerProperty()
    num_angry_reax = ndb.IntegerProperty()

    def add_likes(self):
        for i in range(10):
            self.num_likes+=randint(0,10)
