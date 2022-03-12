import json
import requests
import sys

requests.packages.urllib3.disable_warnings()

headers = { "Accept": "application/yang-data+json",
            "Content-type":"application/yang-data+json"
            }
basicauth = ("cisco", "cisco123!")
sys.stdout = open("Python_Get_Request_Result.txt","w")
#Get IOS Version
api_url0 = "https://192.168.1.3/restconf/data/Cisco-IOS-XE-native:native/version"
resp0 = requests.get(api_url0, auth=basicauth, headers=headers, verify=False)
response0_json = resp0.json()
print(f'IOS Version: \n {response0_json}')
#Get Routing Information
api_url1 = "https://192.168.1.3/restconf/data/Cisco-IOS-XE-native:native/router"
resp1 = requests.get(api_url1, auth=basicauth, headers=headers, verify=False)
response1_json = resp1.json()
print(f'Routing Information: \n {response1_json}')
#Get Interfaces Information
api_url2 = "https://192.168.1.3/restconf/data/Cisco-IOS-XE-native:native/interface"
resp2 = requests.get(api_url2, auth=basicauth, headers=headers, verify=False)
response2_json = resp2.json()
print(f'Interface Information: \n {response2_json}')
sys.stdout.close()