import time
from src.helpers.json_parser import read_configure
from src.helpers.ssh_client import create_client, get_user_pass


def install_requirements(add_packages, client):
    print("Updating...")
    client.exec_command("sudo apt update -y && sudo apt upgrade -y")
    time.sleep(20.0)
    try:
        for package in add_packages:
            print(f"Installing {package}...")
            client.exec_command(f"sudo apt install {package} -y")
            time.sleep(20.0)
    except Exception as e:
        print(e)


def remove_requirements(delete_packages, client):
    try:
        for package in delete_packages:
            print(f"Purging {package}...")
            client.exec_command(f"sudo apt purge {package} -y")
            time.sleep(20)
            client.exec_command("sudo apt autoremove -y")
            time.sleep(15)
    except Exception as e:
        print(e)


def metadata(data, client):
    try:
        for d in data:
            if d['file'][0] == "~":
                file_to_configure = d['file']
            else:
                file_to_configure = f"/var/www/html/{d['file']}"
            if "owner" in d:
                client.exec_command(f"sudo chown -R {d['owner']} {file_to_configure}")
            if "group" in d:
                client.exec_command(f"sudo chgrp -R {d['group']} {file_to_configure}")
            if "mode" in d:
                client.exec_command(f"sudo chmod +{d['mode']} {file_to_configure}")
    except Exception as e:
        print(e)


def configure(file):
    targets, add_packages, delete_packages, data = read_configure(file)
    user, pswd = get_user_pass()
    for target in targets:
        client = create_client(target, user, pswd)
        print(f"Applying configuration on {target}")
        if add_packages:
            install_requirements(add_packages, client)
        if delete_packages:
            remove_requirements(delete_packages, client)
        if metadata:
            metadata(data, client)
        print(f"Rebooting {target}")
        client.exec_command(f"sudo reboot")
        print(f"{target} Complete! \n")
        client.close()


