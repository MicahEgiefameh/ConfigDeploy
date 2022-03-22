from paramiko import SSHClient, AutoAddPolicy
import getpass


def create_client(target):
    client = SSHClient()
    try:
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(target, username='ec2-user', key_filename="~/Downloads/BEEFHOST.pem")
    except:
        #try to get env variable on master, if not ask
        pswd = getpass.getpass('Password:')
        client.connect(target, username='ec2-user', password=pswd)


    return client