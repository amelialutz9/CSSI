import webapp2
import json
import urllib2
import urllib
import os
import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

#  Declare a variable called search_term and initialize it as "puppy".
class MainHandler(webapp2.RequestHandler):
    def get(self):
        search_term = self.request.get("term")
        if search_term == "":
            self.response.write("Please enter a search term.")
        else:
            base_url = "http://api.giphy.com/v1/gifs/search?"
            url_params = {'q': search_term, 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
            giphy_response = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
            parsed_giphy_dictionary = json.loads(giphy_response)
            gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
            self.response.write("<img src="+gif_url+">")


class SearchHandler(webapp2.RequestHandler):
    def get(self):
        my_template = jinja_environment.get_template('templates/search.html')
        self.response.write(my_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/search', SearchHandler)
], debug=True)
