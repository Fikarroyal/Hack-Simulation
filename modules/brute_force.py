class BruteForce:
    def start_cracking(self, username, password_file):
        print(f"Starting brute-force attack on {username} using {password_file}")

        passwords = ["password1", "123456", "admin"]
        for password in passwords:
            print(f"Trying password: {password}")
            if password == "admin":
                print(f"Password found: {password}")
                break
