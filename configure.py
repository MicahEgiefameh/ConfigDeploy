
def install_requirements(add_packages, client):
    client.exec_command("sudo yum update -y && sudo yum upgrade -y")
    try:
        for package in add_packages:
            client.exec_command(f"sudo yum install {package} -y")
    except Exception as e:
        print(e)


def remove_requirements(delete_packages, client):
    try:
        for package in delete_packages:
            client.exec_command(f"sudo yum remove {package} -y")
    except Exception as e:
        print(e)




