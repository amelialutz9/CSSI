#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import ndb
import webapp2
import os
import jinja2
from snack import Snack
from random import randint

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class SnackHandler(webapp2.RequestHandler):
    def get(self):
        snack_kind = self.request.get("kind")
        snack_quantity = self.request.get("quantity")
        snack_rating = self.request.get("rating")
        snack_calories = self.request.get("calories")
        if snack_quantity=="":
            snack_quantity=0
        snack_quantity=int(snack_quantity)
        if snack_rating=="":
            snack_rating=0
        snack_rating=int(snack_rating)
        if snack_calories=="":
            snack_calories=0
        snack_calories=int(snack_calories)
        my_template = jinja_environment.get_template('templates/snack.html')
        render_data={}
        render_data["kind"]=snack_kind
        render_data["quantity"]=snack_quantity
        self.response.write(my_template.render(render_data))
        my_snack = Snack(kind = snack_kind, quantity=snack_quantity, rating=snack_rating, calories=snack_calories)
        my_snack.put()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/snack',SnackHandler)
], debug=True)
