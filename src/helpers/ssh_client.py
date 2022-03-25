from paramiko import SSHClient, AutoAddPolicy
import getpass


def get_user_pass():
    user = input('Target Service User: ')
    pswd = getpass.getpass('Target Service Password: ')
    return user, pswd


def create_client(target, user, pswd):
    client = SSHClient()
    try:
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(target, username=user, password=pswd)
    except:
        print("Error")

    return client