from paramiko import SSHClient, AutoAddPolicy
import getpass


def create_client(target):
    client = SSHClient()
    user = input('Target Service User: ')
    try:
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(target, username=user)
    except:
        pswd = None
        if pswd:
            client.connect(target, username=user, password=pswd)
        else:
            # for multiple Targets, no reentry of password needed
            pswd = getpass.getpass('Target Service Password: ')
            client.connect(target, username=user, password=pswd)


    return client