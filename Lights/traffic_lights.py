import time

class TrafficLights:
    def __init__(self):
        self.state = 'RED'

    def change_state(self):
        if self.state == 'RED':
            self.state = 'GREEN'
        elif self.state == 'GREEN':
            self.state = 'YELLOW'
        elif self.state == 'YELLOW':
            self.state = 'RED'

    def run(self):
        while True:
            print(f'Traffic light state: {self.state}')
            time.sleep(30)  # Simulate traffic light change every 30 seconds
            self.change_state()

if __name__ == "__main__":
    lights = TrafficLights()
    lights.run()
