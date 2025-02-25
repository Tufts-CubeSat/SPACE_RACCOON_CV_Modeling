import time

import requests

# url = "http://10.5.5.9:8080/gopro/camera/analytics/set_client_info"
url = "http://172.23.168.51:8080/gopro/camera/analytics/set_client_info"

# Make sure the url is correct for our camera and its serial number
response = requests.request("GET", url)
print(response.text)

# Enable Wired camera control over USB
url = "http://172.23.168.51:8080/gopro/camera/control/wired_usb"

querystring = {"p": "1"}  # enum where 1 enables usb control, 0 disables it

response = requests.request("GET", url, params=querystring)
if response.status_code == 200:
    print("Wired USB control enabled.")
else:
    print(f"Failed to enable wired USB control: {response.status_code}")

# Keep alive status
url = "http://172.23.168.51:8080/gopro/camera/keep_alive"

response = requests.request("GET", url)

print(response.text)


# Get Media File Info
# url = "http://172.23.168.51:8080/gopro/media/info"

# querystring = {"path":"100GOPRO/GOPR0002.JPG"}

# response = requests.request("GET", url, params=querystring)

# print(response.text)

# turn on raw
url = "http://10.5.5.9:8080/gopro/camera/setting"
querystring = {"option": "3"}

response = requests.request("GET", url, params=querystring)

print(response.text)

url = "http://172.23.168.51:8080/gopro/camera/shutter/start"
response = requests.request("POST", url)

print(response.text)

# Return path to most recently captured media
print("trying to get media path")
url = "http://172.23.168.51:8080/gopro/media/last_captured"

response = requests.request("GET", url).json()

time.sleep(1)

print("FILE:", response["file"])

url = f"http://172.23.168.51:8080/videos/DCIM/100GOPRO/{response['file']}"

response = requests.request("GET", url)

with open("capture.jpg", "wb") as f:
    f.write(response.content)  # writes to JPEG
