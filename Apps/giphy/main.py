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
import webapp2
import os
import json
import jinja2
import urllib
import urllib2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("templates/giphy.html")
        base_url = "http://api.giphy.com/v1/gifs/search?"
        query = self.request.get("search")
        index = self.request.get("index")
        url_params = {'q': query, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        request_url = base_url + urllib.urlencode(url_params)
        #gives us json
        giphy_response = urllib2.urlopen(request_url)
        giphy_json = giphy_response.read()
        giphy_data = json.loads(giphy_json)
        url = giphy_data['data'][int(index)]['images']['original']['url']
        render_data = {}
        render_data['image_url']=url
        self.response.write(template.render(render_data))


# class SearchHandler(webapp2.RequestHandler):
#     def get(self):
#         template = jinja_environment.get_template("templates/search.html")
#         render_data = {}
#         self.response.write(template.render(render_data))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    #('/search', SearchHandler)
], debug=True)
