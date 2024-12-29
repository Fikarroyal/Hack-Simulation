from core.cracker import Cracker
from core.network import Network
from modules.brute_force import BruteForce
from targets.server import Server
from utils.logger import Logger

def main():
    logger = Logger()
    logger.log("Simulation started")

    server = Server("192.168.1.1")
    network = Network(server)
    cracker = Cracker()

    logger.log("Scanning for vulnerabilities...")
    vulnerabilities = network.scan_for_vulnerabilities()

    if vulnerabilities:
        logger.log("Vulnerabilities found, starting exploit...")
        exploit = network.exploit(vulnerabilities[0])
        logger.log("Exploit successful!")
    else:
        logger.log("No vulnerabilities found.")
    
    brute_force = BruteForce()
    brute_force.start_cracking("admin", "passwords.txt")

if __name__ == "__main__":
    main()
