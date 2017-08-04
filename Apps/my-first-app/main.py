#!/usr/bin/env python
#-*- coding: utf-8 -*-
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
from random import randint
from snack import Snack



#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))



class MainHandler(webapp2.RequestHandler):
    greetings = ["Hola, mundo!", "Bonjour le monde!", "你好，世界!", "안녕, 세상!", "alve, orbis terrarum!", "Hello, world!"]
    def stuffForPage(self):
        num=randint(1,len(self.greetings)-1)
        words=[]
        count=0
        for i in range(num):
            random_Index=randint(0,len(self.greetings)-1)
            random_Add=self.greetings[random_Index]
            if count==0:
                words.append(random_Add)
                count=1
            else:
                is_in_list=False
                for item in words:
                    if random_Add==item:
                        is_in_list=True
                if is_in_list==False:
                    words.append(random_Add)
                else:
                    i-=1
        final=""
        for item in words:
            final+=item+"\n"
        return final

    def get(self):
        response = self.stuffForPage()
        self.response.write(response)


class MilkHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Go get some milk!")


class FruitHandler(webapp2.RequestHandler):
    def get(self):
        ans = "<u>TO BUY:</u></br>"
        num = int(self.request.get("num_fruit"))
        food = str(self.request.get("food"))
        gross_food="rutabaga"
        if food == gross_food:
            ans+="<s>1. %s</s></br>Nothing because %s is disgusting!!!!!"%(gross_food,gross_food)
        else:
            for i in range(num):
                ans += "%s. %s</br>"%(i+1, food)
            if num>20:
                ans +="</br>WOW you <i>REALLY</i> need a LOT of %s"%(food)
        self.response.write(ans)


class ImageHandler(webapp2.RequestHandler):
    def get(self):
        greetings = ["Hola", "Bonjour", "alve", "Hello", "Hallo", "Kaixo"]
        my_template = jinja_environment.get_template('templates/hello-world.html')
        the_name = self.request.get("my_name")
        favorite_color = self.request.get("favorite_color")
        if the_name=="":
            the_name="USER"
        render_data = { 'greeting' : greetings[randint(0,len(greetings)-1)] }
        render_data['name']=the_name
        render_data['color']=favorite_color
        render_data['veggie']=self.request.get("vegetable")
        num=self.request.get("number")
        if num=="":
            num=1
        else:
            num=int(num)
        render_data['count']=num
        self.response.write(my_template.render(render_data))

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
        render_data["rating"]=snack_rating
        render_data["calories"]=snack_calories
        self.response.write(my_template.render(render_data))
        my_snack = Snack(kind = snack_kind, quantity=snack_quantity, rating=snack_rating, calories=snack_calories)
        my_snack.put()


class DisplaySnackHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/dispsnack.html')
        query = Snack.query()
        render_data={}
        render_data['list_of_snacks']=query.fetch()
        self.response.write(my_template.render(render_data))


# class LoginHandler(webabb2.RequestHandler):
#     def get(self):
#         scope = 'user-library-read'
#
#         if len(sys.argv) > 1:
#             username = sys.argv[1]
#         else:
#             print "Usage: %s username" % (sys.argv[0],)
#             sys.exit()
#
#         token = util.prompt_for_user_token(username, scope)
#
#         if token:
#             sp = spotipy.Spotify(auth=token)
#             results = sp.current_user_saved_tracks()
#             for item in results['items']:
#                 track = item['track']
#                 print track['name'] + ' - ' + track['artists'][0]['name']
#         else:
#             print "Can't get token for", username
#         self.response.write("this is loaded")



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/milk', MilkHandler),
    ('/fruit', FruitHandler),
    ('/image', ImageHandler),
    ('/snack', SnackHandler),
    ('/dispsnack', DisplaySnackHandler)
], debug=True)
