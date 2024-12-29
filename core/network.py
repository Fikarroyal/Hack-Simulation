class Network:
    def __init__(self, target):
        self.target = target
    
    def scan_for_vulnerabilities(self):
        print(f"Scanning {self.target.ip} for vulnerabilities...")
        return ["Vulnerability 1", "Vulnerability 2"]
    
    def exploit(self, vulnerability):
        print(f"Exploiting {vulnerability} on {self.target.ip}")
        return True
