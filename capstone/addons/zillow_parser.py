from bs4 import BeautifulSoup
from _private.private import ZILLOW_ID

import locale
import re
import requests

class ZillowParser(object):

    def __init__(self, *args, **kwargs):

        self.address = kwargs['address']
        self.city = kwargs['city']
        self.state = kwargs['state']
        self.zip_code = kwargs['zip']
        self.city_state_zip = None
        self.zillow_id = ZILLOW_ID
        self.address_url = 'http://www.zillow.com/webservice/GetSearchResults.htm?zws-id={0.zillow_id}'.format(self)
        self.zestimate_url = 'http://www.zillow.com/webservice/GetZestimate.htm?zws-id={0.zillow_id}'.format(self)
        self.zpid = None
        self.zestimate = None
        self.lat = None
        self.long = None

    def __str__(self):
        return "{0.address}, {0.city}, {0.state}".format(self)

    def __repr__(self):
        return "{0.__class__.__name__}({0.address}, {0.city}, {0.state})".format(self)

    def clean_address(self):
        """ converts address strings into acceptable URL format for POST request """
        self.address = self.address.strip().replace(' ', '+')
        self.city = self.city.strip()
        self.state = self.state.strip()
        self.city_state_zip = "{}%2C+{}".format(self.city, self.state)
        return None

    def get_zillow_id(self):
        """ retrieves Zillow ZPID from XML API """
        self.clean_address()
        # address format: '2114+Bigelow+Ave&citystatezip=Seattle%2C+WA'
        zillow_url = self.address_url + '&address={0.address}&citystatezip={0.city_state_zip}'.format(self)
        xml_response = requests.post(zillow_url) # get Zillow address info
        soup = BeautifulSoup(xml_response.text, 'lxml') # parse XML response
        zpid = str(soup.zpid) # convert tag object to string
        pattern = r'\d+' # re pattern (inside tag)
        search = re.search(pattern, zpid) # grab zpid from inside tag string
        if search:
            result = search.group() # save result
            self.zpid = result
            return None
        else:
            raise ValueError('Unable to locate a Zillow ID for property. Please check the address and try again')

    def get_zestimate(self):
        """ retrieves Zillow Zestimate from XML API """
        # Zestimate format: 'http://www.zillow.com/webservice/GetZestimate.htm?zws-id=<ZWSID>&zpid=48749425'
        self.get_zillow_id() # get zillow id
        zillow_url = self.zestimate_url + '&zpid={0.zpid}'.format(self) # get url
        xml_response = requests.post(zillow_url) # get Zillow info
        soup = BeautifulSoup(xml_response.text, 'lxml') # parse XML response
        amount = str(soup.amount) # convert tag object to string
        pattern = r'\d+' # re pattern (inside tag)
        search = re.search(pattern, amount) # grab appraisal amount from inside tag string
        result = int(search.group()) # save result, converting to int for currency conversion
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') # set up currency conversion from int
        result = locale.currency(result, grouping=True)
        self.zestimate = result
        return None










