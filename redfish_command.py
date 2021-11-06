from redfish_util import redfish_util
import argparse
import sys

COMMANDS_ALL = {"Systems": ["PowerOn", "PowerForceOff", "PowerForceRestart",
                            "PowerGracefulRestart", "PowerGracefulShutdown",
                            "PowerReboot", "SetOneTimeBoot", "SetUefiShell",
                            "DisableUefiShell"]}

redfish_args = argparse.ArgumentParser()
redfish_args.add_argument('-u', '--url', type=str, required=True)
redfish_args.add_argument('-c', '--command', type=str, required=True)
redfish_args.add_argument('-C', '--category', type=str, required=True)
redfish_args.add_argument('-U', '--username', type=str, required=True)
redfish_args.add_argument('-P', '--password', type=str, required=True)
redfish_args.add_argument('-p', '--payload', type=str, required=False)
redfish_args.add_argument('-k', '--skip-ssl-verification', action='store_false')

args = redfish_args.parse_args()

print(args.skip_ssl_verification)

url = args.url
username = args.username
password = args.password
category = args.category
verify = args.skip_ssl_verification
command  = args.command

if category == "Systems":
  if command in COMMANDS_ALL['Systems']:
    print('command is:', command)
  else:
    print("this command is not supported...")
    sys.exit(10)

rf = redfish_util(url=url, creds=({'username': username, 'password': password}), validate_certs=verify)
rf.get_request()


#redfish_command.py -k --username user --password pass --category Systems --command PowerOn 