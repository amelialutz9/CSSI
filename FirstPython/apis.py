import json
import urllib2

response = urllib2.urlopen("https://uinames.com/api/")

content = response.read()
print "json::"
print content

content_dict = json.loads(content)
print content_dict["region"]
