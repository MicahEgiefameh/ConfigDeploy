import getpass
from typing import Tuple

from paramiko import AutoAddPolicy, SSHClient


def get_user_pass() -> Tuple[str, type(getpass.getpass)]:
    """Retrieves username and password from user"""
    user = input("Target Service User: ")
    pswd = getpass.getpass("Target Service Password: ")
    return user, pswd


def create_client(target, user, pswd) -> SSHClient:
    """Creates SSH client to target"""
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(target, username=user, password=pswd)
    return client
