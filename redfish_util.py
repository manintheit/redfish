# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
import requests
import json

GET_HEADERS = {'accept': 'application/json',
               'OData-Version': '4.0'}
POST_HEADERS = {'content-type': 'application/json',
                'accept': 'application/json',
                'OData-Version': '4.0'}
PATCH_HEADERS = {'content-type': 'application/json',
                 'accept': 'application/json',
                 'OData-Version': '4.0'}


class redfish_util(object):
    def __init__(self, url, creds=None, validate_certs=None, timeout=10):
        self.url = url
        self.service_root = "/redfish/v1"
        self.creds = creds
        self.validate_certs = validate_certs
        self.timeout = timeout

    def _manage_authentication(self):
        if self.creds['username']:
            username = self.creds['username']
            password = self.creds['password']
        return username, password

    def _ssl_verification(self):
        if self.validate_certs is False:
            _ssl_validation = False
        else:
            _ssl_validation = None
        return _ssl_validation

    def _extend_message(self):
        pass

    def get_request(self):
        req_headers = dict(GET_HEADERS)
        username, password = self._manage_authentication()
        ssl_validation = self._ssl_verification()
        try:
            resp = requests.get(self.url, auth=(username, password),
                                verify=ssl_validation, headers=req_headers,
                                timeout=self.timeout, allow_redirects=True)
            print(resp.text)

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)

    def post_request(self):
        req_headers = dict(POST_HEADERS)
        username, password = self._manage_authentication()
        ssl_validation = self._ssl_verification()
        try:
            resp = requests.post(self.url, auth=(username, password),
                                 verify=ssl_validation, headers=req_headers,
                                 timeout=self.timeout, allow_redirects=True)
            print(resp.text)

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)

    def patch_request(self):
        req_headers = dict(PATCH_HEADERS)
        username, password = self._manage_authentication()
        ssl_validation = self._ssl_verification()
        try:
            resp = requests.patch(self.url, auth=(username, password),
                                  verify=ssl_validation, headers=req_headers, 
                                  timeout=self.timeout, allow_redirects=True)
            print(resp.text)

        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)

    def power_management():
        #check power status before do anything
        #check if commnad startswith Power. Ifso , add #Action #Computer.Reset
        #
        pass

    def set_one_time_boot(self, target):
        #set onetime boot to target..once and target is name of a target...
        pass

    def set_uefi_shell(self, payload):
        pass

    def disable_uefi_shell(self, payload):
        #check if uefi shell there....
        #if so, disable uefi.
        pass
