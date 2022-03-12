import json
import requests
import sys

requests.packages.urllib3.disable_warnings()

headers = { "Accept": "application/yang-data+json",
            "Content-type":"application/yang-data+json"
            }
basicauth = ("cisco", "cisco123!")
sys.stdout = open("Python_PUT_Request_Result.txt","w")

api_url = "https://192.168.1.3/restconf/data/ietf-interfaces:interfaces/interface=Loopback102"

sys.stdout = open("Python_PUT_Request_Result.txt","w")
#Create interface Loopback 102
yangConfig ={
	"ietf-interfaces:interface": { 
		"name": "Loopback102", 
		"description": "This is created by Python script", 
		"type": "iana-if-type:softwareLoopback",
		"enabled": True,
		"ietf-ip:ipv4": {
			"address": [
				{
					"ip": "192.168.102.1",
					"netmask": "255.255.255.255"
				}
			]
		},
		"ietf-ip:ipv6": {}
	}
}
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))

#Get Interface Loopback 102 Information
api_url0 = "https://192.168.1.3/restconf/data/ietf-interfaces:interfaces/interface=Loopback102"
resp0 = requests.get(api_url0, auth=basicauth, headers=headers, verify=False)
response0_json = resp0.json()
print(f'Interface Loopback 102: \n {response0_json}')
sys.stdout.close()