import requests
import time

wanted_name = input("Wanted name: ")
password = input("Password: ")
bearer = input("Bearer token: ")
UUID = input("UUID of account to snipe with: ")
dropTime = input("Time to start sniping (input as HH:MM:SS): ")

print("Ok, waiting for time to snipe now . . .")

url = 'http://api.mojang.com/user/profile/' + UUID + '/name'

attempts = 10

while True:
	time_str = time.strftime("%H:%M:%S")
	time.sleep(0.05)
	if time_str == dropTime:
		attempts = attempts - 1
		req = requests.post(url, headers={'Authorization': bearer}, json={"name": wanted_name,"password": password})
		if req.status_code == 204:
			print ("Succesfully sniped the name " + wanted_name + "!")
			break
		if attempts == 0:
			print ("Failed to snipe name")
			break
input()
