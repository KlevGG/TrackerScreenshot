import base64
import configparser
import os
import sys
from getpass import getpass

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

_cached_master_password = None


# Generate a key from the master password
def generate_key():
    # Read the config file
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Get the salt from the config file
    salt = bytes.fromhex(config["settings"]["salt"])
    password = _cached_master_password

    # Derive a key using PBKDF2HMAC
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))
    return key


# Encrypt the 2FA secrets
def encrypt_secrets(secrets):
    key = generate_key()

    fernet = Fernet(key)
    encrypted_secrets = {}
    for tracker, secret in secrets.items():
        if secret == "0":
            encrypted_secrets[tracker] = "0"
        else:
            encrypted_secrets[tracker] = fernet.encrypt(secret.encode("utf-8")).decode(
                "utf-8"
            )
    return encrypted_secrets


# Decrypt the 2FA secrets
def decrypt_secrets(encrypted_secrets):
    key = generate_key()

    fernet = Fernet(key)
    decrypted_secrets = {}
    for tracker, encrypted_secret in encrypted_secrets.items():
        if encrypted_secret == "0":
            decrypted_secrets[tracker] = "0"
        else:
            decrypted_secrets[tracker] = fernet.decrypt(
                encrypted_secret.encode("utf-8")
            ).decode("utf-8")
    return decrypted_secrets


def get_cached_master_password():
    global _cached_master_password
    return _cached_master_password


def get_decrypted_secrets():
    global _cached_master_password

    # Read the secrets file, create it if it doesn't exist
    if not os.path.exists("secrets.ini"):
        with open("secrets.ini", "w") as secretsfile:
            secretsfile.write("[secrets]\n")
    secrets_config = configparser.ConfigParser()
    secrets_config.read("secrets.ini")

    # Read the config file
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Verify the master password
    if _cached_master_password is None:
        _cached_master_password = getpass("Enter the master password: " + "\n")

    master_password_hash = config["settings"]["master_password"]
    ph = PasswordHasher()
    try:
        ph.verify(master_password_hash, _cached_master_password)
    except VerifyMismatchError:
        sys.exit(1)

    # Decrypt the secrets
    encrypted_secrets = secrets_config["secrets"]
    decrypted_secrets = decrypt_secrets(encrypted_secrets)

    return decrypted_secrets
