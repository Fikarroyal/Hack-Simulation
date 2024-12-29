class Server:
    def __init__(self, ip):
        self.ip = ip
    
    def respond(self, request):
        print(f"Server at {self.ip} responding to {request}")
