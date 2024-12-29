class Device:
    def __init__(self, device_name, ip):
        self.device_name = device_name
        self.ip = ip
    
    def connect(self):
        print(f"Connecting to device {self.device_name} at {self.ip}")
