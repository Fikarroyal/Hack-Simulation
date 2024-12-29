from cryptography.fernet import Fernet

class Encryption:
    def generate_key(self):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key
    
    def encrypt_message(self, message, key):
        fernet = Fernet(key)
        encrypted = fernet.encrypt(message.encode())
        return encrypted
    
    def decrypt_message(self, encrypted_message, key):
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_message).decode()
        return decrypted
