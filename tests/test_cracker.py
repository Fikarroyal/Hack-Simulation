import unittest
from core.cracker import Cracker

class TestCracker(unittest.TestCase):
    def test_start_cracking(self):
        cracker = Cracker()
        cracker.start_cracking("admin", "passwords.txt")

if __name__ == "__main__":
    unittest.main()
