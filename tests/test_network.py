import unittest
from core.network import Network
from targets.server import Server

class TestNetwork(unittest.TestCase):
    def test_scan_for_vulnerabilities(self):
        server = Server("192.168.1.1")
        network = Network(server)
        vulnerabilities = network.scan_for_vulnerabilities()
        self.assertTrue(len(vulnerabilities) > 0)

if __name__ == "__main__":
    unittest.main()
