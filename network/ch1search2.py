import urllib, urllib2
try:
    import json
except ImportError:  # for Python 2.5
    import simplejson as json

params = {'address': '207 N. Defiance St, Archbold, OH',
          'sensor': 'false'}
url = ('http://maps.googleapis.com/maps/api/geocode/json?'
       + urllib.urlencode(params))

rawreply = urllib2.urlopen(url).read()

reply = json.loads(rawreply)
print reply['results'][0]['geometry']['location']
