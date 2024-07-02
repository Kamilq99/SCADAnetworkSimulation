import time
import requests

PLC_URL = "http://plc:5000/update"

def main():
    while True:
        data = {"command": "change_light"}
        response = requests.post(PLC_URL, json=data)
        if response.status_code == 200:
            print("Command sent to PLC")
        else:
            print("Failed to send command to PLC")
        time.sleep(30)  # Send command every 30 seconds

if __name__ == "__main__":
    main()