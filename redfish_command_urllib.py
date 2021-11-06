#redfish_command.py --baseuri https://..... --username user --password password --category Systems --command PowerOff --validate_certs False
#redfish_command.py --category Systems --command SetOneTimeBoot --uefi_target uefishell
#redfish_command.py --category Systems --command EnableUefiShell
from urllib import request
import ssl
import argparse




GET_HEADERS = {'accept': 'application/json', 'OData-Version': '4.0'}
POST_HEADERS = {'content-type': 'application/json', 'accept': 'application/json', 'OData-Version': '4.0'}
PATCH_HEADERS = {'content-type': 'application/json', 'accept': 'application/json', 'OData-Version': '4.0'}

COMMANDS_ALL = { "Systems": ["PowerOn", "PowerForceOff", "PowerForceRestart", "PowerGracefulRestart",
                "PowerGracefulShutdown", "PowerReboot", "SetOneTimeBoot", "SetUefiShell", "DisableUefiShell"]
              }


class redfish_command(object):
    def __init__(self, url, validate_certs=None, username=None, password=None):
        self.url = url
        self.service_root = "/redfish/v1"
        self.validate_certs = validate_certs
        self.username = username
        self.password = password
        self.validate_certs = validate_certs

    def _ssl_verification(self):
        if self.validate_certs is False:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
        else:
            ctx = None
        return ctx

    def auth_method():
        pass

    def read_request(self):
        ctx = self._ssl_verification()
        #req_headers = dict(GET_HEADERS)
        resp = request.urlopen(self.url, context=ctx)
        print(resp.read())

    def post_request(self):
        pass

    def patch_request(self):
        pass



rf = redfish_command('http://wp.manintheit.org')
rf.read_request()