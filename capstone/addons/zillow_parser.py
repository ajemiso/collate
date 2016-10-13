from bs4 import BeautifulSoup
from lxml import etree
from _private.private import ZILLOW_ID

import requests


class ZillowParser:

    def __init__(self, *args, **kwargs):
        self.address = None
        self.city_state_zip = None

    def get_address_id(self):

        # address format: '2114+Bigelow+Ave&citystatezip=Seattle%2C+WA'
        response = requests.post('http://www.zillow.com/webservice/GetSearchResults.htm?zws-id={zillow_id}'
                                 '&address={address}&citystatezip={city_state_zip}'.format(zillow_id=ZILLOW_ID,
                                                                                           address=self.address,
                                                                                           city_state_zip=
                                                                                           self.city_state_zip,
                                                                                            ))
        xml_response = etree.XML(response)



