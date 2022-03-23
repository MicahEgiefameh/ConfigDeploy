from config_deploy.json_parser import read_configure
from ssh_client import create_client


def install_requirements(add_packages, client):
    client.exec_command("sudo yum update -y && sudo yum upgrade -y")
    try:
        for package in add_packages:
            client.exec_command(f"sudo yum install {package} -y")
        client.exec_command(f"sudo service apache2 restart")
    except Exception as e:
        print(e)


def remove_requirements(delete_packages, client):
    try:
        for package in delete_packages:
            client.exec_command(f"sudo yum remove {package} -y")
    except Exception as e:
        print(e)


def metadata(data, client):
    try:
        for key, value in data.items():
            file_to_configure = key
            if "owner" in value:
                client.exec_command(f"sudo chown -R {value['owner']} {file_to_configure}")
            if "group" in value:
                client.exec_command(f"sudo chgrp -R {value['group']} {file_to_configure}")
            if "mode" in value:
                client.exec_command(f"sudo chmod +{value['mode']} {file_to_configure}")
    except:
        print("Couldnt complete")


def configure(file):
    targets, add_packages, delete_packages, data = read_configure(file)
    for target in targets:
        client = create_client(target)
        install_requirements(add_packages, client)
        if delete_packages:
            remove_requirements(delete_packages, client)
        if metadata:
            metadata(data, client)