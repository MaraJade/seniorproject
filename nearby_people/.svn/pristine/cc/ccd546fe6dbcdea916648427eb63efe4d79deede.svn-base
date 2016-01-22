# New GeoNames library from Greg Robbins
# See https://github.com/gregrobbins/geonames-python
# This is the fork https://github.com/Gagravarr/geonames-python

import sys
import urllib
import urllib2
try:
    from simplejson import loads as json_parse
except ImportError:
    from json import read as json_parse

DOMAIN = 'http://api.geonames.org/'
USERNAME = '' #enter your geonames username here
DEBUG = 0

def fetchJson(method, dparams):
    # GeoNames supports the same arguments multiple times, eg 
    #  featureClass=["P","T"] -> featureClass=P&featureClass=T
    # We need to switch from a dict to array so that urllib will send that
    params = []
    for key, value in dparams.items():
         # One or many values?
         if isinstance(value, basestring) or isinstance(value, int):
             params.append((key,value))
         else:
             for v in value:
                 params.append((key,v))
    # urllib doesn't like unicode strings, so change those to utf8
    for i in range(len(params)):
        kv = params[i]
        if isinstance(kv[1], unicode):
           params[i] = (kv[0], kv[1].encode('utf-8'))
    # Build the url
    uri = DOMAIN + '%s?%s&username=%s' % (method, urllib.urlencode(params), USERNAME)
    if DEBUG:
        print uri
    resource = urllib2.urlopen(uri).readlines()
    js = json_parse(resource[0])
    if DEBUG:
        print js
    return js

def get(geonameId, **kwargs):
    method = 'getJSON'
    valid_kwargs = ('lang',)
    params = {'geonameId': geonameId}
    for key in kwargs:
        if key in valid_kwargs:
            params[key] = kwargs[key]
    return fetchJson(method, params)

def children(geonameId, **kwargs):
    method = 'childrenJSON'
    valid_kwargs = ('maxRows', 'lang',)
    params = {'geonameId': geonameId}
    for key in kwargs:
        if key in valid_kwargs:
            params[key] = kwargs[key]
    results = fetchJson(method, params)

    if('geonames' in results):
        return results['geonames']
    elif('status' in results and 'message' in results['status']):
        raise IOError(results['status']['message'])
    else:
        return None

def search(**kwargs):
    method = 'searchJSON'
    valid_kwargs = ('q', 'name', 'name_equals', 'name_startsWith', 'maxRows', 'startRow', 'country', 'countryBias', 'continentCode', 'adminCode1', 'adminCode2', 'adminCode3', 'featureClass', 'featureCode', 'lang', 'type', 'style', 'isNameRequired', 'tag', 'operator', 'charset',)
    params = {}
    for key in kwargs:
        if key in valid_kwargs:
            params[key] = kwargs[key]
    results = fetchJson(method, params)

    if('geonames' in results):
        return results['geonames']
    elif('status' in results and 'message' in results['status']):
        raise IOError(results['status']['message'])
    else:
        return None

def postalCodeSearch(**kwargs):
    method = 'postalCodeSearchJSON'
    valid_kwargs = ('postalcode', 'postalcode_startsWith', 'placename', 'placename_startsWith', 'maxRows', 'country', 'countryBias', 'style', 'operator', 'isReduced', 'charset',)
    params = {}
    for key in kwargs:
        if key in valid_kwargs:
            params[key] = kwargs[key]
    results = fetchJson(method, params)

    if('postalCodes' in results):
        return results['postalCodes']
    elif('status' in results and 'message' in results['status']):
        raise IOError(results['status']['message'])
    else:
        return None

def findNearbyPostalCodes(**kwargs):
    method = 'findNearbyPostalCodesJSON'
    valid_kwargs = ('postalcode', 'placename', 'maxRows', 'country', 'localCountry', 'lat', 'lng', 'radius', 'style',)
    params = {}
    for key in kwargs:
        if key in valid_kwargs:
            params[key] = kwargs[key]
    results = fetchJson(method, params)

    if('postalCodes' in results):
        return results['postalCodes']
    elif('status' in results and 'message' in results['status']):
        raise IOError(results['status']['message'])
    else:
        return None

def hierarchy(geonameId, **kwargs):
    method = 'hierarchyJSON'
    valid_kwargs = ('lang')
    params = {'geonameId': geonameId}
    for key in kwargs:
        if key in valid_kwargs:
            params[key] = kwargs[key]
    results = fetchJson(method, params)

    if('geonames' in results):
        return results['geonames']
    elif('status' in results and 'message' in results['status']):
        raise IOError(results['status']['message'])
    else:
        return None
