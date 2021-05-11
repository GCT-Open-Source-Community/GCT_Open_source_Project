import requests
import json

url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/36"

payload={}
headers = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

response = requests.request("GET", url, headers=headers, data=payload)

json_data = response.json()

#print(json_data)

#for i in json_data["districts"]:
	#print(i["district_id"],'\t', i["district_name"])

url1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=725&date=11-05-2021"

payload={}
headers = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}

response1 = requests.request("GET", url1, headers=headers, data=payload)

json_data1 = response1.json()
#print(json_data1)

json_data1 = json_data1["centers"]
#print(json_data1)

for i in range(0,len(json_data1)):
	q = json_data1[i]["sessions"]
	centre =json_data1[i]["center_id"]
	adress = json_data1[i]["address"]
	pincode = json_data1[i]["pincode"]
	for j in range(0,len(q)):
		print(centre)
		print(adress)
		print(pincode)
		#print(q[j])
		print("Session Id"+" "+q[j]["session_id"])
		print("vacine Name is"+" "+q[j]["vaccine"])
		slot = q[j]["slots"]
		for s in slot:
			print(s)
		print()
		print()

