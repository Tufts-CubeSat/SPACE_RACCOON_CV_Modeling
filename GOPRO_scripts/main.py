import time
import requests

IP_ADDRESS = "172.23.168.51:8080"

def confirm_camera_serial():
    url = f"http://{IP_ADDRESS}/gopro/camera/analytics/set_client_info"
    # Make sure the url is correct for our camera and its serial number
    response = requests.request("GET", url)
    return response
    # print(response.text)

def enable_wired_camera():
    # Enable Wired camera control over USB
    url = f"http://{IP_ADDRESS}/gopro/camera/control/wired_usb"
    querystring = {"p": "1"}  # enum where 1 enables usb control, 0 disables it

    response = requests.request("GET", url, params=querystring)
    if response.status_code == 200:
        print("Wired USB control enabled.")
    else:
        print(f"Failed to enable wired USB control: {response.status_code}")

def keep_alive():
# Keep alive status
    url = f"http://{IP_ADDRESS}/gopro/camera/keep_alive"
    response = requests.request("GET", url)
    print(response.text)q


# Get Media File Info
# url = "http://172.23.168.51:8080/gopro/media/info"

# querystring = {"path":"100GOPRO/GOPR0002.JPG"}

# response = requests.request("GET", url, params=querystring)

# print(response.text)

# turn on raw
def enable_raw():
    url = f"http://{IP_ADDRESS}/gopro/camera/setting"
    querystring = {"option": "3"}

    response = requests.request("GET", url, params=querystring)

    print(response.text)

def capture_image():
    url = f"http://{IP_ADDRESS}/gopro/camera/shutter/start"
    response = requests.request("POST", url)
    print(response.text)

def get_recentFile():
# Return path to most recently captured media
    url = f"http://{IP_ADDRESS}/gopro/media/last_captured"
    response = requests.request("GET", url).json()
    time.sleep(1) # TODO: comment why
    print("FILE:", response["file"])

def read_image():
    url = f"http://{IP_ADDRESS}/videos/DCIM/100GOPRO/{response['file']}"
    response = requests.request("GET", url)
    with open("capture.jpg", "wb") as    f:
        f.write(response.content)  # writes to JPEG

def initialize_camera():
    confirm_camera_serial()
    enable_wired_camera()
    enable_raw()
    keep_alive()

if __name__ == "__main__":
    initialize_camera()